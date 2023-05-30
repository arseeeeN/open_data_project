<script>
    import DailyAreaChart from "../components/DailyAreaChart.svelte";
    import SeasonalBarChart from "../components/SeasonalBarChart.svelte";
    import Map from "../components/map/Map.svelte";
</script>

<nav class="flex items-center flex-col pt-10">
    <h1 class="text-7xl font-black">Open Data Project</h1>
    <h1 class="mt-6 mb-12 text-4xl font-bold">Ausfälle im Öffentlichen Verkehr</h1>
</nav>
<p class="text-body">
    <!-- TODO: Rewrite this -->
    Die meisten kennen diese Situation, man ist an der Bushaltestelle und wartet
    auf seinen Bus damit man zum Bahnhof kommt und dort auf den Zug kann. In der App steht
    das der Bus um 08:19 ankommt jedoch ist es bereits 09:21 und es ist kein Bus in Sicht.
    Langsam wird man nervös, ist der Bus vielleicht früher gekommen und man hat ihn verpasst? Nicht möglich,
    er muss also einfach verspätet sein... kommt man noch rechtzeitig am Bahnhof an?
    Fünf Minuten später, insgesamt mit Sieben Minuten Verspätung, kommt der Bus dannn doch an.
    Während der Fahrt wird einem dann langsam klar das der anschliessende Zug bereits abgefahren ist.
    Vielleicht ist der allgegewärtige "Zugausfall wegen Baustelle" einigen doch bekannter.
    <br>
    Im Allgemeinen ist die Häufigkeit dieser Situationen relativ hoch und ich habe mich immer gefragt was die Ursachen für 
    die Verspätungen und Ausfälle sind und wie viele davon denn eigentlich vorkommen und ob dies von der Jahreszeit abhängt.
    Ich werde probieren einige meiner Fragen mit dem Datenset welches ich habe zu beantworten und meine Erkenntnisse zu visualisieren.
</p>
<h2 class="text-4xl font-black my-8">Heatmap</h2>
<p class="text-body">
    Die erste Idee war, die Hotspots für Ausfälle in der Schweiz zu finden.
    Dafür ist eine Heatmap natürlich ideal also sass ich mich an die Arbeit.
    Beim Verarbeiten der Daten sind mir einige Anomalien aufgefallen, auf welche ich später noch genauer eingehen werde.
    Diese Merkwürdigkeiten sind ebenfalls in der Heatmap zu sehen.
    Man kann in der Heatmap die Zeitspanne wählen und nach den Ausfallgründen filtern. Ausserdem hat man noch einige kleine Statistiken.
</p>
<Map />
<p class="text-body">
    Wie man auf den ersten Blick in der Heatmap sehen kann, sehen die Daten wahrscheinlich nicht so aus wie erwartet.
    Was man erwarten könnte, wäre das die grössten Städte in der Schweiz die meisten Ausfälle haben, dies ist aber nur bedingt der Fall.
    Lausanne hat zwar viele Einwohner aber über das ganze Jahr verteilt hat Lausanne in diesem Datenset 45958 Ausfälle
    (und Epalinges, Croisettes welches neben Lausanne liegt hat 45516 Ausfälle) was im Vergleich zu den anderen Standorten
    um einiges mehr ist. Dies lässt sich aber erklären, wenn man sich das Datenset genauer anschaut.
    <br>
    Im Datenset sind hauptsächlich Ausfälle des "Regionalen Personenverkehrs" (RPV), jedoch hat es in einigen Regionen auch Linien
    des Ortsverkehrt (OV). In Zürich jedoch z.B. hat es nur Linien des RPV und somit in der Stadt selbst kaum aufgezeichnete Ausfälle.
    Ein anderer Grund für die Masse der Ausfälle in Lausanne ist die Tatsache das es in Lausanne sehr viele Ausfälle des Typ 2 gibt
    "Keine Echtzeitdaten für ganze Fahrt". Dies heisst, dass wir nicht wissen ob diese Fahrten wirklich ausgefallen sind oder sie einfach nicht richtig
    übertragen worden sind. Indem man Typ 2 bei dem Filter ausschaltet erhält man ein etwas "korrekteres" Bild der ganzen Situation.
</p>
<h2 class="text-4xl font-black my-8">Tägliche Ausfälle</h2>
<p class="text-body">
    Eine simple Statistik die viel aussagen kann ist natürlich die Anzahl täglichen Ausfälle.
    Das Ziel hierbei ist es potenzielle Ereignisse zu erkennen, welche sich in den Daten wiederspiegeln.
</p>
<DailyAreaChart />
<p class="text-body">
    Man sieht im Graphen einige interessante Dinge. Das erste was auffällt ist, dass die Daten generell ziemlich gleichmässig sind
    und nur an einzelnen Orten "Spikes" haben. Der grösste dieser Spikes passiert am 7. und 8. November und es gibt einige kleinere
    um den 10. Dezember und 17. Mai rum. Ich habe zu keinem dieser Daten eine klare Ursache gefunden und man kann lediglich nur spekulieren
    warum es zu so vielen Ausfällen an diesen Tagen kam.
</p>
<h2 class="text-4xl font-black my-8">Seasonale Ausfälle</h2>
<p class="text-body">
    Eine Statistik die mich persönlich brennend interessiert hat ist ob die Ausfälle etwas mit den Jahreszeiten zu tun haben.
    Für mich persönlich wäre es zum Beispiel logisch, dass es im Winter mehr Ausfälle hat wegen Schnee und schlechtem Wetter
    und im Sommer könnte man wegen der Hitze villeicht einen ähnlichen Effekt sehen, schauen wir uns mal an was der Graph sagt!
</p>
<SeasonalBarChart />
<p class="text-body">
    Ich lag scheinbar komplett daneben? Das es im Herbst die meisten Ausfälle hat, hat wahrscheinlich mit dem Spike vom 7. und 8. November zu tun
    jedoch erklärt das nicht warum der Winter so wenige Ausfälle hat? Könnte es sein das ich die Robustheit unseres Öffentliche Verkehrs unterschätzt habe?
    Die plausiblere Erklärung meinerseits wäre jedoch, dass der Hauptgrund für Ausfälle Baustellen sein könnten und es im Winter einfach weniger Baustellen hat.
    Dies ist hierbei nachwievor reine Spekulation meinserseits.
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
        <a class="link" href="https://github.com/arseeeeN/open_data_project">Source</a>
    </div>
    <div>
        <h3 class="font-bold text-lg">Contact</h3>
        <p>Arsenije Jevric</p>
        <a class="link block" href="https://github.com/arseeeeN">GitHub</a>
        <a class="link block" href="https://www.linkedin.com/in/arsenije-jevric-635603269/">LinkedIn</a>
    </div>
</footer>