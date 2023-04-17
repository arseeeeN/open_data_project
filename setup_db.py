import csv, sqlite3

def extract_bpuic(value: str) -> str:
    return value[1:value.find(')')]

setup_query = open('setup_db.sql', 'r').read()
con = sqlite3.connect("./data/open_data.db")
cur = con.cursor()
cur.execute('PRAGMA foreign_keys = ON;')
cur.executescript(setup_query)

with open('data/dienststellen_actualdate.csv','r', encoding="utf8") as f:
    dr = csv.DictReader(f, delimiter=";")
    to_db_didok = [(i['BPUIC'], i['BEZEICHNUNG_OFFIZIELL'], i['E_WGS84'], i['N_WGS84']) for i in dr]
cur.executemany("INSERT INTO didok (BPUIC, BEZEICHNUNG_OFFIZIELL, E_WGS84, N_WGS84) VALUES (?, ?, ?, ?);", to_db_didok)
con.commit()

with open('data/ausfall_ 2022-01-01_2023-03-11.csv','r', encoding="utf8") as f:
    dr = csv.DictReader(f, delimiter=";")
    to_db_ausfall = [(i['betriebstag'], i['ausf_typ_bezeichnung'], extract_bpuic(i['bhf_von']), extract_bpuic(i['bhf_bis'])) for i in dr]
for entry in to_db_ausfall:
    try:
        cur.execute("INSERT INTO ausfall (betriebstag, ausf_typ_bezeichnung, bhf_von, bhf_bis) VALUES (?, ?, ?, ?);", entry)
    except Exception:
        print("Couldn't add ausfall: ", entry)
con.commit()

con.close()