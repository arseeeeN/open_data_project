<script>
    // @ts-nocheck
    import { AreaChart } from "$lib/client/graphs";
    import { onMount } from "svelte";

    export let data = [{
        date: "2007-e4-23",
        close: 93.24
    },{
        date: "2007-e4-24",
        close: 95.35
    },{
        date: "2007-e4-25",
        close: 98.84
    }];
    let element;

    onMount(() => {
        element.appendChild(AreaChart(data, {
            x: d => d.date,
            y: d => d.close,
            yLabel: "↑ Daily close ($)",
            width: 200,
            height: 500,
            color: "steelblue"
        }));
    });
</script>

<div bind:this={element}></div>