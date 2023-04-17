<script>
    // @ts-ignore
    import L from "leaflet";
    import "leaflet-tilelayer-swiss";
    // @ts-ignore
    import HeatmapOverlay from "leaflet-heatmap";
    import { onMount } from "svelte";
    
    onMount(async () => {
        const map = L.map('mapid', {
            crs: L.CRS.EPSG2056,
        });
        
        L.tileLayer.swiss().addTo(map);
        map.fitSwitzerland();
        
        const heatmapData = await fetch('/api/heatmap')
            .then(x => x.json());
        const cfg = {
            radius: 0.0005,
            maxOpacity: 0.8,
            scaleRadius: true,
            useLocalExtrema: false,
            latField: 'N_WGS84',
            lngField: 'E_WGS84',
            valueField: 'amount'
        };
        const heatmapLayer = new HeatmapOverlay(cfg);
        heatmapLayer.addTo(map);
        heatmapLayer.setData({
            max: 10000,
            data: heatmapData,
        });
        console.log(heatmapLayer);
    });
</script>

<h1 class="text-7xl font-black">Open Data Project</h1>
<h1 class="m-6 text-4xl font-bold">Verspätungen und Ausfälle</h1>
<div id="mapid"></div>

<style>
    #mapid {
        height: 30rem;
        width: 50vw;
        margin: 0;
    }
</style>
