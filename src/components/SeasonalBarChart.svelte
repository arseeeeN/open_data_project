<script lang="ts">
    import { BarChart } from "$lib/client/graphs";
    import { onMount } from "svelte";

    let springStart = "";

    let element: HTMLElement;
    
    function aggregateToSeasons(data: any[]): any[] {
        for (const day of data) {
            // TODO: Implement this
        }
        return [];
    }

    onMount(async () => {
        const data = await fetch("/api/daily")
            .then(x => x.json());
        element.appendChild(
            BarChart(data, {
                x: (d: any) => d.season,
                y: (d: any) => d.amount,
                yLabel: "Anzahl Ausfälle",
                yFormat: "%",
                width: 1200,
                height: 500,
                color: "teal"
            } as any)!
        );
    });
</script>

<div class="w-[1200px] h-[500px] my-16" bind:this={element}></div>