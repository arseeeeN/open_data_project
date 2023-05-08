<script lang="ts">
    export let filter: any;
</script>

<h2 class="font-bold mt-6">Filter:</h2>
<label class="label cursor-pointer justify-start">
    <input type="checkbox" bind:checked={filter["1"]} class="checkbox h-5 w-5" />
    <span class="label-text ml-4">1. Ganze Fahrt als Ausfall gemeldet</span>
</label>
<label class="label cursor-pointer justify-start">
    <input type="checkbox" bind:checked={filter["2"]} class="checkbox h-5 w-5" />
    <span class="label-text ml-4">2. Keine Echtzeitdaten für ganze Fahrt</span>
</label>
<label class="label cursor-pointer justify-start">
    <input type="checkbox" bind:checked={filter["3"]} class="checkbox h-5 w-5" />
    <span class="label-text ml-4">3. Ganze Fahrt hat Status Unbekannt</span>
</label>
<label class="label cursor-pointer justify-start">
    <input type="checkbox" bind:checked={filter["4"]} class="checkbox h-5 w-5" />
    <span class="label-text ml-4">4. Ganze Fahrt über Takt</span>
</label>
<label class="label cursor-pointer justify-start">
    <input type="checkbox" bind:checked={filter["5"]} class="checkbox h-5 w-5" />
    <span class="label-text ml-4">5. Keine Echtzeitdaten für Teilstrecke einer Fahrt</span>
</label>
<label class="label cursor-pointer justify-start">
    <input type="checkbox" bind:checked={filter["6"]} class="checkbox h-5 w-5" />
    <span class="label-text ml-4">6. Teilstrecke einer Fahrt hat Status Unbekannt</span>
</label>