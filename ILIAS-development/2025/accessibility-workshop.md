Widget aktivierbar

Keine fokusierbaren Elemente ineinander
Invalide
```html
<li role="tab"><a href="#">Tab Title</a></li>
```
Valide
```html
<li><a role="tab" href="#">Tab Title</a></li>
```

Navigation mit Pfeiltasten auf einer Ebene IST Teil von Zusatzdokumenten der Spezifikation
z.B. Radio Buttons einmal fokussieren, dann Pfeiltasten

Zwingend brauchen fokusmanagement: grid, menu, menubar, tablist, tree, treegrid, application

Bearbeitungsmodi im Screen Reader
Lesemodus - Screen Reader nimmt die meisten Tastendrücke entgegen, alle Tasten sind belegt inkl. Pfeiltasten
Bearbeitungsmodus - Browser nimmt die Tastendrücke entgegen, erlaubt Schreiben und Navigation mit Pfeiltasten

Rollen müssen stimmen, damit Screen Reader entsprechend den Modus wechseln können (z.B. zur Menüsteuerung mit Pfeiltasten)

Menuitems müssen mit Pfeiltasten navigierbar sein

Live Regions werden bei Änderungen sofort vorgelesen erhalten aber keinen Fokus

`<details>` Element mit Summary zum Verbergen von Hilfstexten

Dialog
showModal() setzt Fokus in Modal und sperrt abgedunkelten Bereich der Seite auch für Screen Reader

```html
<dialog open>
  <p>Greetings, one and all!</p>
  <form method="dialog">
    <button>OK</button>
  </form>
</dialog>
```

aria-*
meiste html tags bringen ausreichende semantische Eigenschaften mit
wenns mit html tags geht, besser nur damit

Fokus
```html
<div role="tree">
    <a role="treeitem" tabindex="-1">Item 1</a>
    <a role="treeitem" aria-selected="true">Item 2</a>
    <a role="treeitem" tabindex="-1">Item 3</a>
</div>
```

```html
<div role="tree" aria-activedescendant="item-2" tabindex="0">
    <a role="treeitem" id="item-1">Item 1</a>
    <a role="treeitem" id="item-2" aria-selected="true">Item 2</a>
    <a role="treeitem" id="item-3">Item 3</a>
</div>
```

Der erste Treffer in dieser Kette wird als Label herangezogen:
aria-labeledby > aria-label > HTML elemente (z.B. label oder legend) > title Attribut als Fallback (sowohl für label als auch description)

aria-labledby braucht bei Links auch die Selbstreferenz
```html
<span id="123" class="highlighted-text">Große Rabattaktion</span> <a id="456" href="./details.html" aria-labelledby="456 123">mehr erfahren</a>
<!-- screen reader liest "mehr erfahren Große Rabattaktion" -->
```

aria-describedby z.B. input mit Hilfstext oder Fehlermeldung verknüpfen
Bei Fehlermeldung kann live region UND aria-describedby gleichzeitig Sinn ergeben:
* live region beim Entstehen der Meldung
* aria-describedby, damit es beim hinnavigieren vorgelesen wird
live region zu output feld wird nur vorgelesen, wenn das output Feld schon von anfang an da war und mit textcontent ausgetauscht wird.

```html
<span id="i1">Text 1</span>
<a href="#" aria-labelledby="i1 i2" id="i2"><img src="..." alt="Text 2">Text 3</a>
<!-- screen reader liest "Text 1 Text 2 Text 3" -->
```

Für einfach Namensgebung wenn möglich auf aria-* Auszeichnungen verzichten

Vorschlag zu Lückentext
Im Lesemodus
```html
<span id="i01">Hier ist eine</span> <input id="i02" type="text" aria-label="[Lücke]"> <span id="i03">im Text</span>
```
Für den Bearbeitungsmodus verändern
```html
<span id="i01">Hier ist eine</span> <input id="i02" type="text" aria-describedby="i01 i02 i03" aria-label="[Lücke]"> <span id="i03">im Text</span>
```

öffnende Schaltflächen mit aria-expanded
oder neuer `<details>` html tag

Akkordeons haben eine Überschrift
```html
<details>
    <summary>
        <h2>Überschrift des Akkordeons</h2>
    </summary>
    <p>Text der angezeigt wird</p>
</details>
```

popover target eher nicht nutzen

Veränderung des Kontextes ankündigen z.B. "Fokus wird automatisch vorgerückt bei valider Eingabe" PLZ wirft Cursor in die Stadt Auswahl

Bei Formuelementen wie checkbox erwarten screen reader Nutzer nicht unbedingt, dass diese etwas auslösen (z.B. checkbox.. mit role="switch" zur Wechselschaltfläche machen)

* `<button>`
    * Aktionschaltfläche
    * Umschaltfläche toggle mit aria-pressed
    * Wechselschaltflächen Switch Buttons role="switch" und aria-checked
    * Erweitern und Reduzieren aria-expanded
    * Überblendschaltflächen aria-haspopup

Am Besten direkt button html element nehmen. Nicht-aktive Elemente wie span brauchen dann mindestens noch role="button", tabindex, onkeydown

Aria Label überschreibt sichtbaren Inhalt
````html
<button aria-label="Search through user list">Search</button>
````
"Search" ist gar nicht mehr vorhanden

Lupen Symbol nicht visuell beschreiben, sondern die Aktion 
```html
<button><img src="..." alt="Search user list"></button>
```

Aufpassen bei Play / Pause
entweder
Play / Play aria-pressed="true"
oder
Pause / Play

für image hotspots  aria-has-popup="dialog"
