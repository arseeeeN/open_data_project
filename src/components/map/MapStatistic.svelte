<script lang="ts">
    export let title: string;
    export let tooltip: string;
    export let value: any;
</script>

<div>
    <h2 class="mt-2 text-sm">
        {title}:
        <div class="tooltip z-[999]" 
            data-tip={tooltip}
        >🛈</div>
    </h2>
    <span class="font-bold">{value ?? ""}</span>
</div>