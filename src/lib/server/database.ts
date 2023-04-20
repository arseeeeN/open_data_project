import Database from "better-sqlite3";
import fs from "node:fs";

export const db = new Database(fs.readFileSync("data/open_data.db"), { readonly: true });
db.pragma('journal_mode = WAL');