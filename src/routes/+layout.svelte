<script lang="ts">
    import "../app.css";
    import ThemeSwitcher from "../components/ThemeSwitcher.svelte";

    let theme: string;
</script>

<div class="flex items-center flex-col py-10 min-h-screen" data-theme={theme}>
    <ThemeSwitcher bind:theme={theme} />
    <slot />
</div>