import { json } from "@sveltejs/kit";

import Database from "better-sqlite3";
import fs from "node:fs";

let db = new Database(fs.readFileSync("data/open_data.db"), { readonly: true });
db.pragma('journal_mode = WAL');

export function GET() {
    return json(db
        .prepare(`
            SELECT didok.E_WGS84, didok.N_WGS84, occurrences.amount
            FROM didok
            INNER JOIN (
                SELECT bhf_von, COUNT(*) as amount
                FROM ausfall
                GROUP BY bhf_von
            ) as occurrences
            ON didok.BPUIC = occurrences.bhf_von
        `)
        .all()
    );
}