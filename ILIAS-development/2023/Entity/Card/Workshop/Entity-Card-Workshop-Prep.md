# Vorbereitung

Datum: 30.05.2023

Teilnehmende: Timon, Richard, Ferdinand, Yvonne


# Workshop Anlass

* Ähnlichkeit card und item ist schon früher aufgefallen, im Entity Projekt erneut.
* Einteilung der Informationen in Cards soll klarer definiert werden (Sections vs. semantische Gruppen)

# Workshop Ziel

* Abgrenzung Entity vs. Nicht Entity (Entity vs. Item, Card Entity vs. Card vs. Repo Card)
* Beschluss jetzige Karte umbauen oder neue Entity Card erstellen
* Projekt initiieren (Roadmap anfertigen)

# Leitfrage

* Worin unterscheidet sich Card von Item?

# Ausgangslage

* Card und Item können die gleichen Informationen darstellen
* Mapping Versuch der semantischen Gruppen ist vor allem für Repository Card erfolgsversprechend
* Ähnliche Ideen für "feste Orte" vorhanden (ggf. an einem Grid ausrichten)

# Klassifizierung

* Standard Card vs. Entity Card
* Entity Card = Repository Card

# Actions

* Card hat Call to Action Button
* Dropdown können beide haben
* Semantische Gruppen, Priority Areas, Reihenfolge gibt es bei Actions noch nicht

# Long-term vision

* Semantische Gruppen und Priority Areas könnten helfen, Ansichten mit reduziertem oder hohem Detailgrad zu erzeugen, die User selber bestimmen kann.

# Discussion
* Cards sind ein Ding wo es um den Look geht und nicht um semantische Beschreibungen
* Cards und Deck of Cards stehen zur Zeit noch nebeneinander, inzwischen haben wir schon viel gelernt.
* Cards damals entstanden mit Vorbild "Bootstrap 3", damals gab es sowas wie Modal, Card, Deck of Card -> lange grosses Vorbild für UI Framework. Kritik hat gezeigt, dass es besser ist strukturierter zu beschreiben und ranzugehen. Danach wurden die Dinge umgesetzt als PHP. In System Styles die erste Umsetzung der Deck of Cards, weil es noch nichts gab (Panels und Cards). Rein von der Form getrieben und nicht von der Funktion.
* Lessons learned:
  * Lernkurve, früher eher nach Form. Heute viel mehr nach Funktion arbeiten.
  * Cards "gutes" Erfolgsmodell, haben schnell Einzug gefunden in ILIAS. Aber: Es gab aber auch schnell Issues dazu. -> zeigte, dass Funktion wesentlich wichtiger ist (Aufbau der Cards).
  * Unterscheidung des "Dings" und der "Collection" (Set von Dingen)
* Aktuelle Items sind aktuell zu schwach (Codieren einen Look), es ist nicht klar, wozu wir die brauchen. Es geht um eine Stärkung.
* Sammlung von Entities, die will ich als Sammlung von Cards darstellen (Collections).
* Collection
  * andere Darstellungsform der Entity-Properties
  * wie gehen wir mit der kleineren Darstellungsform um (was passiert mit längeren Inhalten, was zeigen wir an)
* Wie gehen wir mit Entity auf kleineren Bildschirmen um?
  * Card ist eine kleinformatige Darstellung einer Entity, wie es auf kleinen Bildschirmen funktioniert, aber wir stellen sie auch auf grösseren Bildschirmen dar.
* Vorgehen wir bei Entity: Card bestehen lassen, erst Entity anpassen und einführen, danach abschaffen (nicht direkt sagen "es ersetzt die Card", sondern positiv formulieren)

Card vs. Repo Card vs. Entity
* Card und Repo Card "einfrieren" (langsames "Fade-out" initiieren)
* In Richtung Entity arbeiten und gut überlegen, ob nicht eher Entity eingesetzt werden sollte.
* Entity Listing einführen
* Keine Migration
* Inhaltlich ist es dasselbe, Entity ist eine stärker strukturierte Version
* Call to Action wäre auch gut für die Entity
* Lässt sich schwer sagen, ob die aktuellen Verwendungen der Card überführt werden können (weil so schlecht definiert)

Reihenfolge Aktionen
* sehr wahrscheinlich Ähnlichkeit zu Projekt Exercise presentation Table" 
* Verordnung Reihenfolge Aktionen ist falsch für Call-to-Action (ist was primary, sollte nicht versteckt sein), muss eindeutig sein was die gecallte Action ist
* Abgrenzung Call-to-Action vs. Launcher
* Darstellung: Man kann "Kommentar hinzufügen" nicht weniger wichtig machen als "Kurs beitreten". Das Ding bekommt Liste von priorisierter Actions, eine davon ist ausgezeichnet als Call-to-Action.
* Mentals Modell Dateisystem? Rechtsklick "Kopieren", Standardoptionen, Call-to-Actions
* Aktionen die angezeigt werden unterschiedlich je nach Rolle, oder wie ich zu der Entity stehe (wird Button ersetzt?). Wird lohnenswert die Leute zu zwingen, wie viel Abstufungen gibt es, was für Aktionen braucht es jetzt wirklich.
* Bei vielen Screens ist nicht klar, welche Aktion der User ausführen will. Besser Leute erst lernen lassen:
  * 1. Pick
  1. Search
  2. Manage
* Frage offen, ob Aktion zur Entity gehört: Rechte abfragen, Targets, Trennung zu Verwaltung/Manage und Aktionen dort anzeigen
  * "Reduced Listing" könnte helfen, dass der User bessere Übersicht hilft
  * Aktionenmenu zugeständig, dass User "immer zu Settings kommen muss" als Shortcut für Admins, aber wenn Admin-View schneller Zugang, weniger notwendig dass Aktionen
  * Single Actions bei DataTable direkte Manipulation für weniger Aktionen, Magazin sind Arranging Aktionen, die ausserhalb des Objekts stattfinden könnten.
  * Wir müssen die Balance finden, was wir umgesetzt bekommen. Muss nicht sofort angegangen werden. Als long-term-vision.
  * Aktuell schon Aktionen ausserhalb des Objekts und innerhalb sind unterschiedlich.
  * Möglicher Weg denkbar Entity in Card einpflegen.
* Evt. weniger in Card und Item denken, sondern Entity Listing in User Intend kombinieren "Pick Entity".
  * Über Entity sprechen als in einen

Managing View
* Managing View = Tabellenansicht
* Reduzierte Darstellung nur bei "Quick Pick" Intend
* Managing-Screen: Gibt es eine Übersetzung einer Liste zu einer Datentabelle

* Annahme: Eher Ansicht/Listing bestimmt die Ansicht
    * Conditional auf dem Container in dem die Entity liegt.
    * Für die Entity dasselbe HTML darstellen lassen

# Roadmap
* langfristig Abschaffen der Card (depricated und bessere Spezifikation was die UseCases sind)
* neue Verwendung einführen (Entity)
* Usecases gut prüfen, dass Entity das Richtige, allenfalls Alternativen (z.B. SystemStyle per Icon als Bildergalerie, Mitgliedergalerie als Adressbuch kodieren)
* Next step: Auf Basis 5810 (https://github.com/ILIAS-eLearning/ILIAS/pull/5810) neuen PR für Card Entity Listing erstellen. 
  * Wann wechselt man zur Card? Schwerpunkt auf dem Bild (Primary Identifier)
  * Wie übersetzt sich die Gewichtung der Entity auf die Card?
  * Ist es dasselbe wie auf einem kleinen Screen?
  * Wir können nicht klären, welche Gruppen wann angezeigt werden und was da drin ist (müssen Maintainer entscheiden)
  * Es sollte möglich werden langfristig, Entscheidungen treffen zu können, wie viele Eigenschaften dargestellt wird.
  * Ziel: Gesamtheit der Informationen darstellen, mti der Aufforderung nicht immer zu machen (nur da wo notwendig)
* CaT schreibt Angebot an Universität Bern.