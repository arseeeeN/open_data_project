CREATE TABLE didok(
    BPUIC INTEGER PRIMARY KEY,
    BEZEICHNUNG_OFFIZIELL TEXT,
    E_WGS84 REAL,
    N_WGS84 REAL
);

CREATE TABLE ausfall(
    betriebstag INTEGER,
    ausf_typ_bezeichnung TEXT,
    bhf_von INTEGER,
    planzeit_von INTEGER,
    bhf_bis INTEGER,
    planzeit_bis INTEGER,
    FOREIGN KEY(bhf_von) REFERENCES didok(BPUIC),
    FOREIGN KEY(bhf_bis) REFERENCES didok(BPUIC)
);