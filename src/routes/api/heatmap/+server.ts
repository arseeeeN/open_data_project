import { json } from "@sveltejs/kit";
import { db } from "$lib/server/database";

export function GET({ url }) {
    const from = url.searchParams.get("from");
    const to = url.searchParams.get("to");
    let queryCondition = "";
    if (from && to) {
        queryCondition = `
            WHERE
                CASE WHEN planzeit_von IS NOT NULL
                THEN
                    planzeit_von BETWEEN ${from} AND ${to}
                ELSE
                    betriebstag BETWEEN ${from} AND ${to}
                END
        `;
    }
    const filter = url.searchParams.get("filter");
    // This if-check is here for correct behaviour when we get an empty list as a
    // filter param. This happens when we deselected all filter boxes in the frontend.
    if (filter === "") {
        return json({
            data: [],
            max: 0,
            average: 0,
            total: 0,
        });
    }
    if (filter) {
        const filterCondition = filter
            .split(",")
            .map(x => `ausf_typ_bezeichnung LIKE '${x}.%'`)
            .join(" OR ");
        if (queryCondition) {
            queryCondition += ` AND (${filterCondition})`;
        } else {
            queryCondition = `WHERE ${filterCondition}`;
        }
    }
    /* TODO: At the moment the heatmap only displays the starting train stations of
        the cancelled trains, to have more accurate data I should use bhf_von_ausfall
        which would be the bhf from which the train can't continue or is officially 
        cancelled. I should be able to get that info somewhere. If that info isn't
        available for a certain ausfall I can just use bhf_von like I am now */
    const count = db
        .prepare(`
            SELECT didok.E_WGS84, didok.N_WGS84, occurrences.amount
            FROM didok
            INNER JOIN (
                SELECT bhf_von, COUNT(*) AS amount
                FROM ausfall
                ${queryCondition}
                GROUP BY bhf_von
            ) AS occurrences
            ON didok.BPUIC = occurrences.bhf_von
        `)
        .all() as any;
    const metadata = db
        .prepare(`
            SELECT 
                MAX(occurrences.amount) AS max,
                AVG(occurrences.amount) AS average,
                SUM(occurrences.amount) AS total
            FROM (
                SELECT COUNT(*) AS amount
                FROM ausfall
                ${queryCondition}
                GROUP BY bhf_von
            ) AS occurrences
        `)
        .all() as any;
    return json({
        data: count,
        max: Math.ceil(metadata[0].max),
        average: Math.ceil(metadata[0].average),
        total: metadata[0].total,
    });
}