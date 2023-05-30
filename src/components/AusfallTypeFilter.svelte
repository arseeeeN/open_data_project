<script lang="ts">
    export let filter: any;
    export let onChange: () => void = () => {};
</script>

<h2 class="font-bold mt-6">Ausfall Typ Filter:</h2>
<label class="label cursor-pointer justify-start">
    <input type="checkbox" bind:checked={filter["1"]} on:change={onChange} class="checkbox h-5 w-5" />
    <span class="label-text ml-4 flex">
        <b>1.</b>
        <span class="ml-1">Ganze Fahrt als Ausfall gemeldet</span>
    </span>
</label>
<label class="label cursor-pointer justify-start">
    <input type="checkbox" bind:checked={filter["2"]} on:change={onChange} class="checkbox h-5 w-5" />
    <span class="label-text ml-4 flex">
        <b>2.</b>
        <span class="ml-1">Keine Echtzeitdaten für ganze Fahrt</span>
    </span>
</label>
<label class="label cursor-pointer justify-start">
    <input type="checkbox" bind:checked={filter["3"]} on:change={onChange} class="checkbox h-5 w-5" />
    <span class="label-text ml-4 flex">
        <b>3.</b>
        <span class="ml-1">Ganze Fahrt hat Status Unbekannt</span>
    </span>
</label>
<label class="label cursor-pointer justify-start">
    <input type="checkbox" bind:checked={filter["4"]} on:change={onChange} class="checkbox h-5 w-5" />
    <span class="label-text ml-4 flex">
        <b>4.</b>
        <span class="ml-1">Ganze Fahrt über Takt</span>
    </span>
</label>
<label class="label cursor-pointer justify-start">
    <input type="checkbox" bind:checked={filter["5"]} on:change={onChange} class="checkbox h-5 w-5" />
    <span class="label-text ml-4 flex">
        <b>5.</b>
        <span class="ml-1">Keine Echtzeitdaten für Teilstrecke einer Fahrt</span>
    </span>
</label>
<label class="label cursor-pointer justify-start">
    <input type="checkbox" bind:checked={filter["6"]} on:change={onChange} class="checkbox h-5 w-5" />
    <span class="label-text ml-4 flex">
        <b>6.</b>
        <span class="ml-1">Teilstrecke einer Fahrt hat Status Unbekannt</span>
    </span>
</label>