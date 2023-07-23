<script>
    // @ts-nocheck
    import L from "leaflet";
    import "leaflet-tilelayer-swiss";
    import HeatmapOverlay from "leaflet-heatmap";
    import AusfallTypeFilter from "../AusfallTypeFilter.svelte";
    import MapStatistic from "./MapStatistic.svelte";
    import { onMount } from "svelte";
    
    let heatmapLayer;
    let from;
    let to;
    let filter = {
        "1": true,
        "2": true,
        "3": true,
        "4": true,
        "5": true,
        "6": true,
    };
    let average;
    let total;

    function updateHeatmap(heatmapData) {
        average = heatmapData.average;
        total = heatmapData.total;
        heatmapLayer.setData({
            // I don't know enough statistics to use a proper formula here, this is good enough for now
            max: (heatmapData.average + heatmapData.max * 50 * (heatmapData.average / heatmapData.max)) / 2,
            data: heatmapData.data,
        });
    }

    async function handleUpdateEvent() {
        const fromTimestamp = Date.parse(from);
        const toTimestamp = Date.parse(to);
        const filterParam = Object.keys(filter)
            .filter(key => !!filter[key]);
        const url = `/api/heatmap?from=${fromTimestamp}&to=${toTimestamp}&filter=${filterParam}`;
        const heatmapData = await fetch(url)
            .then(x => x.json());
        console.log(heatmapData);
        updateHeatmap(heatmapData);
    }

    const dateSpanFetch = fetch('/api/timespan')
        .then(x => x.json())
        .then(x => { from = x.from; to = x.to; return x });

    onMount(async () => {
        const map = L.map('heatmap', {
            crs: L.CRS.EPSG2056,
            zoomSnap: 1,
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

<div class="card lg:card-side lg:w-[75vw] my-14 bg-base-100 lg:drop-shadow-xl items-center">
    <div class="h-[30rem] lg:h-auto w-full lg:flex lg:items-center m-0 lg:rounded-l" id="heatmap"></div>
    <div class="card-body max-w-fit min-w-3/5">
        <h2 class="card-title">Einstellungen</h2>
        <div class="flex flex-col lg:flex-row lg:gap-10">
            <div class="pr-4 lg:p-0">
                {#await dateSpanFetch}
                    <div class="loading"></div>
                {:then timeSpan}
                    <h2 class="font-bold mt-6">Zeitspanne:</h2>
                    <div class="form-control mt-2">
                        <label for="from-time" class="text-sm pl-2 pb-1">From</label>
                        <input type="datetime-local" id="from-time"
                            class="input input-bordered rounded-lg min-w-full"
                            name="from-time" bind:value={from}
                            on:change={handleUpdateEvent}
                            min={timeSpan.from} max={timeSpan.to}>
                    </div>
                    <div class="form-control mt-2">
                        <label for="to-time" class="text-sm pl-2 pb-1">To</label>
                        <input type="datetime-local" id="to-time"
                            class="input input-bordered rounded-lg min-w-full"
                            name="to-time" bind:value={to}
                            on:change={handleUpdateEvent}
                            min={timeSpan.from} max={timeSpan.to}>
                    </div>
                {/await}
                <h2 class="font-bold mt-6">Statistik:</h2>
                <div class="flex mb-4 gap-8">
                    <MapStatistic
                        title="Total"
                        tooltip="Totale Anzahl Ausfälle in dieser Zeitspanne"
                        bind:value={total}
                    />
                    <MapStatistic
                        title="Durchschnitt"
                        tooltip="Durchschnittliche Anzahl Ausfälle pro Bahnhof
                            mit mindestens einem Ausfall in dieser Zeitspann"
                        bind:value={average}
                    />
                </div>
            </div>
            <div class="lg:w-56">
                <AusfallTypeFilter bind:filter={filter} onChange={handleUpdateEvent} />
            </div>
        </div>
    </div>
</div>