<script>
    import DailyAreaChart from "../components/DailyAreaChart.svelte";
    import SeasonalBarChart from "../components/SeasonalBarChart.svelte";
    import Map from "../components/map/Map.svelte";
</script>

<nav class="flex items-center flex-col pt-10">
    <h1 class="text-7xl font-black">Open Data Project</h1>
    <h1 class="mt-6 mb-12 text-4xl font-bold">Verspätungen und Ausfälle</h1>
</nav>
<p class="text-body">
    Die meisten kennen diese Situation, man ist an der Bushaltestelle und wartet 
    auf seinen Bus damit man zum Bahnhof kommt und dort auf den Zug kann. In der App steht
    das der Bus um <b>08:19</b> ankommt jedoch ist es bereits <b>09:21</b> und es ist kein Bus in Sicht.
    <br>
    Langsam wird man nervös, ist der Bus vielleicht früher gekommen und man hat ihn verpasst? Nicht möglich,
    er muss also einfach verspätet sein... kommt man noch rechtzeitig am Bahnhof an?
    <br>
    Fünf Minuten später, insgesamt mit Sieben Minuten Verspätung, kommt der Bus dannn doch an.
    Während der Fahrt wird einem dann langsam klar das der anschliessende Zug bereits abgefahren ist.
    <br>
    Vielleicht ist der allgegewärtige "Zugausfall wegen Baustelle" einigen doch bekannter. Im allgemeinen ist 
    die Häufigkeit dieser Situationen relativ hoch und ich habe mich immer gefragt was die Ursachen für 
    die Verspätungen und Ausfälle sind und wie viele davon denn eigentlich vorkommen und ob dies von der Jahreszeit abhängt.
    <br>
    Ich werde probieren einige meiner Fragen mit dem Datenset welches ich habe zu beantworten und meine Erkenntnisse zu visualisieren.
</p>
<h2 class="text-4xl font-black my-8">Heatmap</h2>
<p class="text-body">
    Die erste Idee war, die Hotspots für Ausfälle in der Schweiz zu finden.
    Dafür ist eine Heatmap natürlich ideal also sass ich mich an die Arbeit.
    <br>
    Beim Verarbeiten der Daten sind mir einige Anomalien aufgefallen, auf welche ich später noch genauer eingehen werde.
    Diese Merkwürdigkeiten sind ebenfalls in der Heatmap zu sehen.
    <br>
    Man kann in der Heatmap die Zeitspanne wählen und nach den Ausfallgründen filtern. Ausserdem hat man noch einige kleine Statistiken.
</p>
<Map />
<p class="text-body">
    Wie man auf den ersten Blick in der Heatmap sehen kann, sehen die Daten wahrscheinlich nicht so aus wie erwartet.
</p>
<h2 class="text-4xl font-black my-8">Tägliche Ausfälle</h2>
<p class="text-body">
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vel enim elit. 
    Nullam sed lorem fringilla, eleifend ante dictum, molestie velit. 
    Quisque porta magna tempor tellus laoreet, a elementum ex auctor. 
    Donec eget odio quis tortor cursus elementum. 
    Fusce ullamcorper nisi eu tortor placerat, nec molestie elit iaculis. 
    Nulla facilisi. Phasellus dignissim est sit amet dapibus fringilla. 
    Proin a leo molestie, feugiat nisi vitae, porta nisl. 
    Proin sit amet nunc in dolor rutrum consectetur. 
    Morbi faucibus orci est, at porttitor justo placerat et. 
    Aenean efficitur metus nec sodales consequat. 
    Quisque efficitur, erat sit amet lacinia condimentum, ipsum quam placerat dolor, eget tincidunt sapien lectus at velit. 
    Sed mattis hendrerit urna, vel rutrum tortor mattis nec.
    Aliquam sed tempor justo, et ornare neque. 
    Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
</p>
<DailyAreaChart />
<p class="text-body">
    Proin non consectetur leo, in sollicitudin arcu. 
    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. 
    Sed a odio quis est porttitor accumsan eu non lectus. 
    Etiam ac est vulputate dui suscipit cursus at eu lectus. 
    Proin ullamcorper, lorem nec rhoncus finibus, turpis magna porta nulla, at pellentesque dui arcu vel mauris. 
    Sed consequat vestibulum ipsum non laoreet. 
    Sed scelerisque pellentesque sapien eget condimentum. 
    Donec ultrices tortor mauris, vel placerat mauris consequat in. 
    Etiam quis libero porta, vestibulum massa ut, sodales ligula.
</p>
<h2 class="text-4xl font-black my-8">Seasonale Ausfälle</h2>
<p class="text-body">
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vel enim elit. 
    Nullam sed lorem fringilla, eleifend ante dictum, molestie velit. 
    Quisque porta magna tempor tellus laoreet, a elementum ex auctor. 
    Donec eget odio quis tortor cursus elementum. 
    Fusce ullamcorper nisi eu tortor placerat, nec molestie elit iaculis. 
    Nulla facilisi. Phasellus dignissim est sit amet dapibus fringilla. 
    Proin a leo molestie, feugiat nisi vitae, porta nisl. 
    Proin sit amet nunc in dolor rutrum consectetur. 
    Morbi faucibus orci est, at porttitor justo placerat et. 
    Aenean efficitur metus nec sodales consequat. 
    Quisque efficitur, erat sit amet lacinia condimentum, ipsum quam placerat dolor, eget tincidunt sapien lectus at velit. 
    Sed mattis hendrerit urna, vel rutrum tortor mattis nec.
    Aliquam sed tempor justo, et ornare neque. 
    Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
</p>
<SeasonalBarChart />
<p class="text-body">
    Proin non consectetur leo, in sollicitudin arcu. 
    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. 
    Sed a odio quis est porttitor accumsan eu non lectus. 
    Etiam ac est vulputate dui suscipit cursus at eu lectus. 
    Proin ullamcorper, lorem nec rhoncus finibus, turpis magna porta nulla, at pellentesque dui arcu vel mauris. 
    Sed consequat vestibulum ipsum non laoreet. 
    Sed scelerisque pellentesque sapien eget condimentum. 
    Donec ultrices tortor mauris, vel placerat mauris consequat in. 
    Etiam quis libero porta, vestibulum massa ut, sodales ligula.
</p>
<h2 class="text-4xl font-black my-8">Fazit</h2>
<p class="text-body">
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vel enim elit. 
    Nullam sed lorem fringilla, eleifend ante dictum, molestie velit. 
    Quisque porta magna tempor tellus laoreet, a elementum ex auctor. 
    Donec eget odio quis tortor cursus elementum. 
    Fusce ullamcorper nisi eu tortor placerat, nec molestie elit iaculis. 
    Nulla facilisi. Phasellus dignissim est sit amet dapibus fringilla. 
    Proin a leo molestie, feugiat nisi vitae, porta nisl. 
    Proin sit amet nunc in dolor rutrum consectetur. 
    Morbi faucibus orci est, at porttitor justo placerat et. 
    Aenean efficitur metus nec sodales consequat. 
    Quisque efficitur, erat sit amet lacinia condimentum, ipsum quam placerat dolor, eget tincidunt sapien lectus at velit. 
    Sed mattis hendrerit urna, vel rutrum tortor mattis nec.
    Aliquam sed tempor justo, et ornare neque. 
    Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
</p>
<footer class="h-44 w-full mt-20 bg-base-200 tracking-wide flex justify-between pt-8 px-40">
    <div>
        <h3 class="font-bold text-lg">Open Data Project</h3>
        <a class="link" href="https://github.com/arseeeeN/open-data-project">Source</a>
    </div>
    <div>
        <h3 class="font-bold text-lg">Contact</h3>
        <p>Arsenije Jevric</p>
        <a class="link block" href="https://github.com/arseeeeN">GitHub</a>
        <a class="link block" href="https://www.linkedin.com/in/arsenije-jevric-635603269/">LinkedIn</a>
    </div>
</footer>