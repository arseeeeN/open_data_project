<script>
    import DailyAreaChart from "../components/DailyAreaChart.svelte";
    import SeasonalBarChart from "../components/SeasonalBarChart.svelte";
    import Map from "../components/map/Map.svelte";
</script>

<nav class="flex items-center flex-col pt-10 text-center mt-14">
    <h1 class="text-7xl font-black">Open Data Project</h1>
    <h1 class="mt-6 mb-12 text-4xl font-bold">Ausfälle im Öffentlichen Verkehr</h1>
</nav>
<p class="text-body">
    Die meisten von uns kennen diese Situation: Man sitzt im Zug und muss bald umsteigen,
    aber beim Blick auf die App stellt man fest, dass der Anschlusszug ausgefallen ist.
    Verzweifelt sucht man nach Alternativen, doch leider ohne Erfolg. Frustriert akzeptiert
    man schliesslich die Niederlage und wartet auf den nächsten Zug.
    <br>
    Manchmal wird diese Situation noch absurder, wenn der ausgefallene Zug plötzlich mit erheblicher Verspätung auftaucht.
    Man fragt sich dann, was wohl die Ursachen für diese Verspätungen und Ausfälle sind
    und wie häufig sie tatsächlich vorkommen. Hängen sie mit dem Wetter oder der Jahreszeit zusammen?
    Zudem stellt sich die Frage, wie viele der offiziell gemeldeten "Ausfälle" tatsächlich komplette Ausfälle
    sind und nicht nur massive Verspätungen oder Kommunikationsprobleme.
    Ich werde probieren diese Fragen mit Hilfe des erhaltenen Datensets zu beantworten und meine Erkenntnisse anschaulich zu visualisieren.
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
    des "Ortsverkehrs" (OV). In Zürich jedoch z.B. hat es nur Linien des RPV und somit in der Stadt selbst kaum aufgezeichnete Ausfälle.
    Ein anderer Grund für die Menge an Ausfällen in Lausanne ist die Tatsache das es in Lausanne sehr viele Ausfälle des Typ 2 gibt
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
    um den 10. Dezember und 17. Mai rum. Der grosse Spike im November hat mich am meisten interessiert und scheinbar war die Ursache dafür
    eine Panne bei der IT von SBB was darin resultierte, dass keine Pünktlichkeitsdaten gespeichert werden konnten. Daher werden die Daten
    als ein Typ 2 Ausfall klassifiziert, die dazugehörigen Fahrten haben zum grössten Teil jedoch wahrscheinlich stattgefunden.
    Wie auch bei der Heatmap kann man hier den Typ 2 bei den Filtern ausschalten um ein korrekteres Bild zu bekommen.
</p>
<h2 class="text-4xl font-black my-8">Saisonale Ausfälle</h2>
<p class="text-body">
    Eine Statistik die mich persönlich brennend interessiert hat ist ob die Ausfälle etwas mit den Jahreszeiten zu tun haben.
    Für mich persönlich wäre es zum Beispiel logisch, dass es im Winter mehr Ausfälle hat wegen Schnee und schlechtem Wetter
    und im Sommer könnte man wegen der Hitze vielleicht einen ähnlichen Effekt sehen, schauen wir uns mal an was der Graph sagt!
</p>
<SeasonalBarChart />
<p class="text-body">
    Ich lag scheinbar komplett daneben? Das es im Herbst die meisten Ausfälle hat, hat wahrscheinlich mit dem Spike vom 7. und 8. November zu tun
    jedoch erklärt das nicht warum der Winter so wenige Ausfälle hat? Könnte es sein das ich die Robustheit unseres Öffentlichen Verkehrs unterschätzt habe?
    Die plausiblere Erklärung meinerseits wäre jedoch, dass der Hauptgrund für Ausfälle Baustellen sein könnten und es im Winter einfach weniger Baustellen hat.
    Dies ist hierbei nach wie vor reine Spekulation meinerseits.
</p>
<h2 class="text-4xl font-black my-8">Fazit</h2>
<p class="text-body">
    Meine Fragen konnten nicht vollständig beantwortet werden, jedoch habe ich trotzdem einige interessante Dinge herausgefunden. Das analysieren der
    Daten war eine interessante Angelegenheit und zu sehen wie viele der Ausfälle einfach nur fehlende Echtzeitdaten sind und welche tatsächlich
    ausgefallen sind. Es ist plötzlich nicht mehr so fragwürdig, das ausgefallene Züge doch noch mit Verspätung auftauchen können.
    <br>
    In der Zukunft würde ich diese Daten gerne noch auf andere Arten visualisieren und sie noch mit Verspätungsdaten verbinden um zu sehen wie diese
    Statistiken zusammenhängen.
</p>
<footer class="footer p-10 mt-20 bg-base-200">
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