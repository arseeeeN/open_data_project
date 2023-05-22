<script lang="ts">
    import { BarChart } from "$lib/client/graphs";
    import { onMount } from "svelte";

    type Season = "Spring" | "Summer" | "Autumn" | "Winter";
    interface SeasonalData {
        season: Season;
        amount: number;
    }

    // Seasons of the year 2022
    let springStart = 1647730800000;
    let summerStart = 1655762400000;
    let autumnStart = 1663884000000;
    let winterStart = 1671663600000;

    let element: HTMLElement;
    
    function aggregateToSeasons(data: any[]): any[] {
        const seasonalData: SeasonalData[] = [
            { season: 'Spring', amount: 0 },
            { season: 'Summer', amount: 0 },
            { season: 'Autumn', amount: 0 },
            { season: 'Winter', amount: 0 },
        ];
        for (const entry of data) {
            const day = entry.betriebstag;
            if (day < springStart) {
                seasonalData[3].amount += entry.amount;
            } else if (day > springStart && day < summerStart) {
                seasonalData[0].amount += entry.amount;
            } else if (day > summerStart && day < autumnStart) {
                seasonalData[1].amount += entry.amount;
            } else if (day > autumnStart && day < winterStart) {
                seasonalData[2].amount += entry.amount;
            } else if (day > winterStart) {
                seasonalData[3].amount += entry.amount;
            }
        }
        return seasonalData;
    }

    onMount(async () => {
        const data = await fetch("/api/daily")
            .then(x => x.json());
        element.appendChild(
            BarChart(aggregateToSeasons(data), {
                x: (d: any) => d.season,
                y: (d: any) => d.amount,
                yLabel: "Anzahl Ausfälle",
                yFormat: "s",
                width: 1200,
                height: 500,
                color: "teal"
            } as any)!
        );
    });
</script>

<div class="w-[1200px] h-[500px] my-16" bind:this={element}></div>