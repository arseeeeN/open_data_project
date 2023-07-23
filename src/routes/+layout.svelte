<script lang="ts">
    import "../app.css";
    import ThemeSwitcher from "../components/ThemeSwitcher.svelte";

    let theme: string;
    $: document.body.setAttribute("data-theme", theme);
</script>

<div class="flex items-center flex-col min-h-screen" data-theme={theme}>
    <ThemeSwitcher bind:theme={theme} />
    <slot />
</div>