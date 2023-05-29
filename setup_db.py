import csv, sqlite3, time
import os
from datetime import datetime
from typing import Union

verbose = False

db_path = './data/open_data.db'
if os.path.exists(db_path):
    print("Deleting the old database file...")
    os.remove(db_path)
setup_query = open('setup_db.sql', 'r').read()
con = sqlite3.connect(db_path)
cur = con.cursor()
cur.execute('PRAGMA foreign_keys = ON;')
cur.executescript(setup_query)

# Read the full data for didok and create a temp dict for later filtering the valid entries
temp_didok = {}

def parse_gueltigkeit(date: str) -> Union[int, None]:
    date_time = datetime.strptime(date, '%Y-%m-%d')
    try:
        return int(time.mktime(date_time.timetuple())) * 1000
    except:
        return None

with open('data/dienststellen_full.csv','r', encoding="utf8") as f:
    dr = csv.DictReader(f, delimiter=";")
    for i in dr:
        bpuic = i['BPUIC']
        gueltig_von = parse_gueltigkeit(i['GUELTIG_VON'])
        gueltig_bis = parse_gueltigkeit(i['GUELTIG_BIS'])
        if not gueltig_von or not gueltig_bis:
            continue
        entry = (
            i['BPUIC'],
            i['BEZEICHNUNG_OFFIZIELL'],
            i['E_WGS84'],
            i['N_WGS84'],
            gueltig_von,
            gueltig_bis
        )
        if bpuic in temp_didok:
            temp_didok[bpuic].append(entry)
        else:
            temp_didok[bpuic] = [entry]

# Read the actual "ausfall" data and make a list for adding it to the database
def extract_bpuic(value: str) -> str:
    return value[1:value.find(')')]

def parse_betriebstag(date: str) -> int:
    date_time = datetime.strptime(date, '%d.%m.%Y')
    return int(time.mktime(date_time.timetuple())) * 1000

def parse_planzeit(date: str) -> Union[int, None]:
    if date == '':
        return None
    date_time = datetime.strptime(date[:-4], '%Y-%m-%d %H:%M:%S')
    return int(time.mktime(date_time.timetuple())) * 1000

with open('data/ausfall_ 2022-01-01_2023-03-11.csv','r', encoding="utf8") as f:
    dr = csv.DictReader(f, delimiter=";")
    to_db_ausfall = [(
        parse_betriebstag(i['betriebstag']),
        i['ausf_typ_bezeichnung'],
        extract_bpuic(i['bhf_von']),
        parse_planzeit(i['planzeit_von']),
        extract_bpuic(i['bhf_bis']),
        parse_planzeit(i['planzeit_bis'])
    ) for i in dr]
    
# Filter the didok entries based on the validity period
to_db_didok = {}

def filter_condition_didok(entry: tuple, time: int):
    gueltig_von = entry[-2]
    gueltig_bis = entry[-1]
    return time > gueltig_von and time < gueltig_bis

count_didok_misses = 0
def filter_and_add_didok_entries(bpuic: str, time: int):
    if bpuic in temp_didok:
        result = list(filter(lambda x: filter_condition_didok(x, time), temp_didok[bpuic]))
        if len(result) != 1:
            global count_didok_misses
            count_didok_misses += 1
            if verbose:
                print("Error, there here has to be exactly one valid entry in the didok, found:", len(result))
        else:
            to_db_didok[bpuic] = result[0][:-2]
    else:
        if verbose:
            print("The BPUIC:", bpuic, "doesn't exist in the supplied didok")

if verbose:
    print("Length of temp didok:", len(temp_didok))
for i in to_db_ausfall:
    # Using indices to access these values is a recipe for disaster
    # but I am too lazy to use dicts here, so this will do
    bhf_von = i[2]
    planzeit_von = i[3]
    if bhf_von and planzeit_von and bhf_von not in to_db_didok:
        filter_and_add_didok_entries(bhf_von, planzeit_von)
    bhf_bis = i[4]
    planzeit_bis = i[5]
    if bhf_bis and planzeit_bis and bhf_bis not in to_db_didok:
        filter_and_add_didok_entries(bhf_bis, planzeit_bis)

if verbose:
    print("Didok misses:", count_didok_misses)
    print("Final length of didok:", len(to_db_didok))

# Commit everything to the database
failed_didok_count = 0
for entry in to_db_didok:
    try:
        cur.execute('INSERT INTO didok (BPUIC, BEZEICHNUNG_OFFIZIELL, E_WGS84, N_WGS84) VALUES (?, ?, ?, ?);', to_db_didok[entry])
    except Exception:
        failed_didok_count += 1
        if verbose:
            print('Couldn\'t add didok:', entry, 'Error during database insert')
if verbose and failed_didok_count > 0:
    print('Couldn\'t add', failed_didok_count, 'didok entries')
con.commit() 

failed_ausfall_count = 0
for entry in to_db_ausfall:
    try:
        cur.execute('INSERT INTO ausfall (betriebstag, ausf_typ_bezeichnung, bhf_von, planzeit_von, bhf_bis, planzeit_bis) VALUES (?, ?, ?, ?, ?, ?);', entry)
    except Exception:
        failed_ausfall_count += 1
        if verbose:
            print('Couldn\'t add ausfall:', entry, 'Error during database insert')
if verbose and failed_ausfall_count > 0:
    print('Couldn\'t add', failed_ausfall_count, 'ausfall entries')
con.commit()

print("Successfully created the database!")
con.close()