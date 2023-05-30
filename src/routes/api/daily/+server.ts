import { json } from "@sveltejs/kit";
import { db } from "$lib/server/database";

export function GET({ url }) {
    let queryCondition = "";
    const filter = url.searchParams.get("filter");
    // This if-check is here for correct behaviour when we get an empty list as a
    // filter param. This happens when we deselected all filter boxes in the frontend.
    if (filter === "") {
        return json([]);
    }
    if (filter) {
        const filterCondition = filter
            .split(",")
            .map(x => `ausf_typ_bezeichnung LIKE '${x}.%'`)
            .join(" OR ");
        queryCondition = `WHERE ${filterCondition}`;
    }
   return json(db
        .prepare(`
            SELECT betriebstag, COUNT(*) as amount
            FROM ausfall
            ${queryCondition}
            GROUP BY betriebstag
        `)
        .all());
}