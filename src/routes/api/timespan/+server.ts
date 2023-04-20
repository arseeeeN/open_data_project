import { json } from "@sveltejs/kit";
import { db } from "$lib/server/database";

export function GET() {
    const result = db
        .prepare(`
            SELECT 
                MIN(MIN(planzeit_von), MIN(betriebstag)) AS min,
                MAX(MAX(planzeit_von), MAX(betriebstag)) AS max
            FROM ausfall
        `)
        .all() as any[];
    return json({
        from: parseTimestamp(result[0]['min']),
        to: parseTimestamp(result[0]['max']),
    });
}

function parseTimestamp(timestamp: number): string {
    return new Date(timestamp)
        .toISOString()
        .slice(0, -5);
}