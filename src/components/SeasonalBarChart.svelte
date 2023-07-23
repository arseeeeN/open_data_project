<script lang="ts">
    import { BarChart } from "$lib/client/graphs";
    import { onMount } from "svelte";
    import AusfallTypeFilter from "./AusfallTypeFilter.svelte";

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
    let filter: { [key: string]: boolean } = {
        "1": true,
        "2": true,
        "3": true,
        "4": true,
        "5": true,
        "6": true,
    };
    
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

    async function handleUpdateEvent() {
        element.removeChild(element.children[0]);
        const filterParam = Object.keys(filter)
            .filter(key => !!filter[key]);
        const url = `/api/daily?filter=${filterParam}`;
        const data = await fetch(url)
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

<div class="card lg:card-side lg:w-[75vw] my-14 bg-base-100 lg:drop-shadow-xl items-center">
    <div class="w-full lg:flex lg:items-center aspect-[12/5] lg:my-16 lg:ml-16 px-2 lg:p-0" bind:this={element}></div>
    <div class="card-body">
        <h2 class="card-title">Einstellungen</h2>
        <AusfallTypeFilter bind:filter={filter} onChange={handleUpdateEvent} />
        <div class="flex gap-10">
        </div>
    </div>
</div>