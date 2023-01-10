---
theme : "white"
transition: "slide"
highlightTheme: "monokai"
logoImg: "img/logo.png"
slideNumber: false
title: "Item Properties"
---

# Properties auf dem UI item

---

## Ausgangssituation

* UI item und Listing Panel sollen das legacy item und Container Object im Repository ablösen {.fragment .fade-in-then-semi-out}
* Dem UI item fehlen dafür vermeintlich Funktionen (Aufklappen, Vorbedingungen) {.fragment .fade-in-then-semi-out}
* aber 1:1 Reproduktion ist nicht Ziel: Beste Übersicht und Bedienung für häufigsten User Intent {.fragment .fade-in-then-semi-out}

---

## Basis

[UX Guide for Repository Object Properties](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/src/UI/docu/ux-guide-repository-objects-properties-and-actions.md)

[Mockups mit grober semantischer Aufteilung](https://catenglaender.github.io/il-item-mockup/new-item-card-structure/)

[Sammlung Excel Mappe](https://cat06.sharepoint.de/:x:/r/sites/Design322/_layouts/15/Doc.aspx?sourcedoc=%7B30326381-8D27-43FC-A7B0-BE5C63FBA015%7D&file=Orte%20und%20Funktionen%20von%20Elementen%20der%20UI%20Componenten.xlsx&action=default&mobileredirect=true&DefaultItemOpen=1)

Feature Requests

[Container Objects to Standard Listing Panel](https://docu.ilias.de/goto.php?target=wiki_1357_Transfering_Container_Objects_to_Standard_Listing_Panel)

[Transfer Repository Objects to KS Items](https://docu.ilias.de/goto_docu_wiki_wpage_6409_1357.html)

[Streamline item Properties](https://docu.ilias.de/goto_docu_wiki_wpage_7399_1357.html)

---

## Häufige User Intents in ILIAS

* Making a quick choice {.fragment .fade-in-then-semi-out}
* Comparing before choosing {.fragment .fade-in-then-semi-out}
* Managing multiple objects {.fragment .fade-in-then-semi-out}

---

## Häufigster User Intent

in einem gut sortiert ILIAS
* für User: Making a quick choice {.fragment .fade-in-then-semi-out}
* für Admins: Managing multiple objects {.fragment .fade-in-then-semi-out}

---

## Vorschlag für Workshop Focus

---

### Bewerten und Sortierung sämtlicher Properties und Elemente

mit Richtlinien für die Anzeige auf dem Item

---

* Anzeigeformat / Datentyp (Datum) {.fragment .fade-in-then-semi-out}
* Konkrete Properties für welches Objekt? (Ablaufdatum Kurs) {.fragment .fade-in-then-semi-out}
* Semantische Gruppen (Ablaufdatum: kein Hauptdidentifikationsmerkmal, aber Interaktionsfaktor) {.fragment .fade-in-then-semi-out}
* Priorität der konkreten Properties für häufigste/n User Intent/s (Ablaufdatum wird wichtiger je näher es kommt) {.fragment -> maßgeblich für die Gestaltung .fade-in-then-semi-out}

---

### Unsere Aufgaben?

* Alle Anzeigeformate / Datentypen, Semantische Gruppen, Prioritätsstufen (für quick choice?) finden und definieren {.fragment .fade-in} 
* Die wichtigsten (alle?) Objekttypen anschauen und deren Properties einordnen {.fragment .fade-in} 
* nebenbei visuelle Konzepte anskizzieren, mit Wireframes visuell denken {.fragment .fade-in} 
* Technische Fragen - DOM Struktur? {.fragment .fade-in}

---

### Anzeigeformat / Datentyp

* Text bevorzugt als 1-Zeiler
* Text Mehrzeiler unbeschränkt
* Text beschränkt auf x-Zeilen
* 1 Wort Status
* Tags
* Key: Value (beides kein Link)
* Key: Value (beides zusammen ein Link)
* Key: Value (Value ist Link)
* Key: Value A, Value B, ...
* Key: Value A, Value B, ... (Values jeweils unterschiedliche Links)
* Icon
* Zahl
* Datum (zig mögliche Anzeigeweisen)
* Bild
* Thumbnail mit Lupe, ruft Modal mit voller Bildgröße auf
* Sternebewertung
* Wort mit Badge
* Icon mit Badge
* Liste von Unterobjekten
* Aufklappbarer Bereich
* Progress Meter (Tacho)

Spezialfälle
* andere Objekte
* Aufklappbare Bereiche
* Modals auslösen (Notizen, Kommentare)

---

Zu Bedenken
* Datum kann für Menschen schwer aufzulösen sein
    * Verfügbarkeit: 01.01.2023 - 31.08.2023
    * verfügbar ab 01.01.
    * verfügbar bis 31.08.

---

* Link
    * kein Link
    * ganzer Property
    * Teil vom Property
* Linkziel
    * zum zugehörigen Objekt
    * zu bestimmten Bereich im Objekt
    * zu Unterobjekten
    * zu verbundenen Objekten

---

Objekttypen

siehe Liste im FR "Streamline Object Properties"

---

## Dokumentation

* Ergebnisse sichern (Fotos von Flipcharts, Sammlungen u.ä.)

Semantische Gruppen und Prioritätsstufen
* Ziel
* Definitionen
* Problematische Fälle

Headerbereich von item ähnlich wie header im Kurs (spricht für Kommentar Icons)

Beschränkungen für Fokusbereich
* Fokus Primary darf 1, Focus Secondary 2 Angaben

Springende Properties? Wenn die Logik gut gemacht ist, fällt es nicht auf, weil die Info dort hinspringt, wo man es braucht

Regeln für Fokusbereich statt allgemein primary, secondary auf Typ einschränken
Focus Date
Focus Personal
Focus Precondition
oder doch Primary, Secondary, Headerbar mit deutlichen Empfehlung

Dynamische Veränderung ist ein gewöhnungsbedürftiges neues Konzept

Regeln setzen für guten Standard, Maintainer definiert Logik für sein Objekt, wenn so etwas gewünscht ist.

Nebenschauplätze
Magazin Gruppieren nach