import { json } from "@sveltejs/kit";
import { db } from "$lib/server/database";

export function GET() {
   return json(db
        .prepare(`
            SELECT betriebstag, COUNT(*) as amount
            FROM ausfall
            GROUP BY betriebstag
        `)
        .all());
}