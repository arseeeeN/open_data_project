CREATE TABLE didok(
    BPUIC INTEGER PRIMARY KEY,
    BEZEICHNUNG_OFFIZIELL  TEXT,
    E_WGS84 REAL,
    N_WGS84 REAL
);

CREATE TABLE ausfall(
    id_fahrt INTEGER PRIMARY KEY,
    betriebstag     TEXT,
    ausf_typ_bezeichnung TEXT,
    bhf_von INTEGER,
    bhf_bis INTEGER,
    FOREIGN KEY(bhf_von) REFERENCES didok(BPUIC),
    FOREIGN KEY(bhf_bis) REFERENCES didok(BPUIC)
);