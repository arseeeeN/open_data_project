<script>
    // @ts-nocheck
    import L from "leaflet";
    import "leaflet-tilelayer-swiss";
    import HeatmapOverlay from "leaflet-heatmap";
    import { onMount } from "svelte";
    
    let heatmapLayer;
    let from;
    let to;
    let average;
    let total;

    function updateHeatmap(heatmapData) {
        average = heatmapData.average;
        total = heatmapData.total;
        heatmapLayer.setData({
            max: (heatmapData.average + heatmapData.max * 0.3) / 2,
            data: heatmapData.data,
        });
    }

    async function handleUpdatePress() {
        const fromTimestamp = Date.parse(from);
        const toTimestamp = Date.parse(to);
        const url = `/api/heatmap?from=${fromTimestamp}&to=${toTimestamp}`;
        const heatmapData = await fetch(url)
            .then(x => x.json());
        console.log(heatmapData);
        updateHeatmap(heatmapData);
    }

    const dateSpanFetch = fetch('/api/timespan')
        .then(x => x.json())
        .then(x => { from = x.from; to = x.to; return x });

    onMount(async () => {
        const map = L.map('mapid', {
            crs: L.CRS.EPSG2056,
        });
        
        L.tileLayer.swiss().addTo(map);
        map.fitSwitzerland();
        
        const heatmapData = await fetch('/api/heatmap')
            .then(x => x.json());
        console.log(heatmapData);
        const cfg = {
            radius: 0.0005,
            maxOpacity: 0.8,
            scaleRadius: true,
            useLocalExtrema: false,
            latField: 'N_WGS84',
            lngField: 'E_WGS84',
            valueField: 'amount'
        };
        heatmapLayer = new HeatmapOverlay(cfg);
        heatmapLayer.addTo(map);
        updateHeatmap(heatmapData);
    });
</script>

<div class="card w-[70vw] card-side bg-base-100 drop-shadow-xl">
    <div id="mapid"></div>
    <div class="card-body">
        {#await dateSpanFetch}
            <div class="loading"></div>
        {:then timeSpan}
            <h2 class="card-title">Einstellungen</h2>
            <div class="form-control w-full max-w-xs mt-2">
                <label for="from-time" class="text-sm pl-2 pb-1">From</label>
                <input type="datetime-local" id="from-time"
                    class="input input-bordered rounded-lg w-full max-w-xs"
                    name="from-time" bind:value={from}
                    min={timeSpan.from} max={timeSpan.to}>
            </div>
            <div class="form-control w-full max-w-xs mt-2">
                <label for="to-time" class="text-sm pl-2 pb-1">To</label>
                <input type="datetime-local" id="to-time"
                    class="input input-bordered rounded-lg w-full max-w-xs"
                    name="to-time" bind:value={to}
                    min={timeSpan.from} max={timeSpan.to}>
            </div>
            {#if total}
                <div>
                    <h2 class="mt-4 text-sm">
                        Total:
                        <div class="tooltip z-[999]"
                            data-tip="Totale Anzahl Ausfälle in dieser Zeitspanne"
                        >🛈</div>
                    </h2>
                    <span class="font-bold">{total}</span>
                </div>
            {/if}
            {#if average}
                <div>
                    <h2 class="mt-4 text-sm">
                        Durchschnitt:
                        <div class="tooltip z-[999]" 
                            data-tip="Durchschnittliche Anzahl Ausfälle pro Bahnhof
                            mit mindestens einem Ausfall in dieser Zeitspanne"
                        >🛈</div>
                    </h2>
                    <span class="font-bold">{average}</span>
                </div>
            {/if}
            <div class="card-actions justify-end mt-auto">
                <button on:click={handleUpdatePress} class="btn btn-primary">Update</button>
            </div>
        {/await}
    </div>
</div>

<style>
    #mapid {
        height: 30rem;
        width: 50vw;
        margin: 0;
        border-top-left-radius: var(--rounded-box, 1rem);
        border-bottom-left-radius: var(--rounded-box, 1rem);
    }
</style>