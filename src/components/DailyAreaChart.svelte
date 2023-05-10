<script lang="ts">
    import { AreaChart } from "$lib/client/graphs";
    import { onMount } from "svelte";

    let element: HTMLElement;

    onMount(async () => {
        const data = await fetch("/api/daily")
            .then(x => x.json());
        element.appendChild(
            AreaChart(data, {
                x: (d: any) => d.betriebstag,
                y: (d: any) => d.amount,
                yLabel: "Tägliche Ausfälle",
                width: 1200,
                height: 500,
                color: "teal"
            } as any)!
        );
    });
</script>

<div class="w-[1200px] h-[500px] my-16" bind:this={element}></div>