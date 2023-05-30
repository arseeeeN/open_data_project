<script lang="ts">
    import { AreaChart } from "$lib/client/graphs";
    import { onMount } from "svelte";
    import AusfallTypeFilter from "./AusfallTypeFilter.svelte";

    let element: HTMLElement;
    let filter: { [key: string]: boolean } = {
        "1": true,
        "2": true,
        "3": true,
        "4": true,
        "5": true,
        "6": true,
    };

    async function handleUpdateEvent() {
        element.removeChild(element.children[0]);
        const filterParam = Object.keys(filter)
            .filter(key => !!filter[key]);
        const url = `/api/daily?filter=${filterParam}`;
        const data = await fetch(url)
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
    }

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
<div class="card w-[85vw] h-[38rem] my-14 card-side bg-base-100 drop-shadow-xl items-center">
    <div class="w-[1200px] h-[500px] my-16 ml-16" bind:this={element}></div>
    <div class="card-body h-full">
        <h2 class="card-title">Einstellungen</h2>
        <AusfallTypeFilter bind:filter={filter} onChange={handleUpdateEvent} />
        <div class="flex gap-10">
        </div>
    </div>
</div>