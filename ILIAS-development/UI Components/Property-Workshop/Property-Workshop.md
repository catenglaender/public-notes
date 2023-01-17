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


Semantische Gruppen und Prioritätsstufen
* Ziel
* Definitionen
* Problematische Fälle

---

## Starting point

* Objects with **many properties in the repository are hard to read** because of high information density.
* This makes identifying the right object at a glance challenging and **slows down navigation.**
* Therefor, we propose a set of semantic groups and a priority system for **ordering item properties by intuitive understanding and relevance** to help the average user find what they are looking for with greater ease.

## Scope within the roadmap
* This proposal adresses some challenges of the following in-demand feature requests: Replace the Object in Repositories, Streamline Object Properties
* The UI item and UI listing panel need some additional features anyway to fully replace the legacy object. Adding the semantic groups and priority fields could be done during this overhaul.
* We outline suggestions and reasons why some features of the legacy object should be dropped or substituted with a more simple solution on the UI item as they are covered by other UI components and dedicated views.

## Considering User Intent
Instead of displaying all properties in the same area of the UI item we propose seperating the properties into semantic groups that falls in line with the user's focus.

To better estimate how the user processes the properties we have to assume the needs and expectations that most users have while browsing the repository.

* The majority of users are not administrators or managing users, but learners trying to access relevant objects as quickly as possible. In the [UX Guide for Repository Object Properties](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/src/UI/docu/ux-guide-repository-objects-properties-and-actions.md), this user intent type is labled "making a quick choice".
* Following the guidelines, we suggest optimizing for quick identification and access for the average user and not for administrative operations.
* Other UI components like the UI presentation table and UI table are better suited for administrative user intents as outlined in the aforementioned UX Guide.
* We second that the Manage- and Sorting-Views of the repository should be further optimized for carrying out administrative operations as the user self-identified the user intent of a managing user when activating these modes.

## Semantic groups
The following definitions for semantic groups were the result of a two day workshop with participants from the University of Bern, Leifos GmbH and CaT Concepts and Training GmbH filled with discussions, brainstorming as well as experimenting with examples and mockups building on input from community proposals, feature requests, past CSS Squad and UI Clinic meetings.

* The categories are sorted in the order they should be percieved by the average user browsing the repository with a quick choice user intent.
* The semantic groups were developed with a focus on common properties displayed on repository objects with the use on UI items in mind. For a list of properties the feature request [Streamline Object Properties](https://docu.ilias.de/goto_docu_wiki_wpage_7399_1357.html) was tremendously helpful.
* We do believe that the same or similar categories could also be applied to sort properties displayed in UI cards, UI presentation tables, info tabs, tools and sidebars.

### Main Identifiers
* ...make an object uniquely and quickly identifiable for a human.
* If the managing user creating this object sets the Main Identifiers with care, a user browsing to find it should be able to make accurate assumptions about the content from these properties alone.

**Examples:** Title, Icon, tile image, Thumbnail, Date (e.g. for sessions)

**Non-Examples:** An ID meant for identification of the object in the database

### Personal Status
* These properties indicate the status of a releation between the current user and the object.
* The provided information generally changes through multiple phases,
* is personalized and
* highly relevant when re-visiting an object.
* The user can take direct and indirect actions to influence these values.
* Status about the absence of something ("Certificate: no certificate") should generally not be rendered especially if it is redundant - unless this information is highly relevant for the average user ("Learning process: not started").

**Examples:** Learning Progress, certificate, submission status

**Non-Examples:** Indicators of general social media type interactions and links to other objects directly generated by the current user such as comments, notes, tags (in their current individualized implementation), pin/like/favorite are Reaction properties

### Availability
* Properties that could potentially limit a users access to the object belong to this group.

**Examples:** Availability dates, available seats, offline/online visibility, preconditions, registration dates

### Main Descriptors
* ...are properties describing the content that a user can expect within the object or other relevant attributes
* usually manually set by the managing user.

**Examples:** description text, tags (if they are carefully set by a managing user), custom meta-data if relevant to the average user (e.g. room number for a lecture), other web apps sometimes show categories here.

**Non-Example:** Tags as they are currently implemented have more of a personal note purpose, can be spammed by other users and should therefor be tucked away in the Reactions category. Often times custom meta-data like license information is only relevant for managing users and should not be displayed on repository items.

### Reactions
* ...are social media type ways for a user to quickly mark or react to the object.
* Some reactions are visible to the entire community, others are private to the current user.
* Coincidentally, most of the Reactions are currently already grouped as a row of icons with badges in the header of an opened object.

**Examples:** comments, notes, personal tags, pin/like/favorite

**Non-Examples:** a submission is a personal interaction with the object, but not a social media type reaction

### Generated Meta-Data
This is meta-data not manually set or changable by the user or administrator.

* **Example:** Number of pages, creation date, file type
* **Non-example:** Offline/Online visibility as it can be manually checked

## Priority areas
The semantic groups should be visually weighted from most to least important on the UI item, to make split-second decisions for the most common use cases easier.

However, in some cases, a specific property from a less important group might become as important as a Main Identifier. 

For example, if there is a restriction preventing a user from accessing the object, they would probably like to see this as early as possible. Other times, a specific property can provide key information a user would prefer to know before interacting with the object - like the type and size of a file object.

For these cases, we propose priority areas that can pull single properties from certain groups to a featured position.

### Primary Identifier
* One of the Main Identifiers must be pulled to the most important, highest-priority position.
* This is the attribute that a user is generally supposed to see first.

**Example:** Title, Tile Image, Session Date

### Secondary Identifier
* This can be filled with a Main Identifier that the user is supposed to see second most of the time.

**Example:** Icon, Event Date, File Preview Thumbnail

### Blocking Preconditions
* If there is a condition from the Availability properties that prevents the user from accessing or interacting with the object, it should be displayed here. By placing the information why an object is locked in this prominent position, we avoid confusion about why the user is not able to open it.
* There are cases where an object shows an availability property when the object is available (when there are seats left or within the availability and registration period date range), but often times they end up in this featured area.

**Example:** Offline visibility, outside of availability or registration period, registration period expired

### Leading Properties
* Sometimes a detail might be critical information to sway the user's split-decision to interact with an object or not.
* In this case a property from any of the groups can be pulled into this featured position and present it as the most important property of the rest of the properties.
* It is expected that all objects prioritize different properties here, as different objects offer vastly different functionality.
* Optionally, there may be a logic picking different properties conditionally. For example, before joining a course a user might find a highlighted registration deadline useful, but after registration the approaching end of availability gains priority and is therefor highlighted instead.

**Example:** File type and size for file objects, registration and availability deadline for users

### Prioritized Reaction

* For certain objects we might want to present a reaction property more prominently and position it apart from the other ones.

**Example:** Star rating

## Guidleines for displaying properties
No redundancy, if one property implies another

## Discarded concepts

### Expandable area
After careful consideration we decided to discourage a collapsable and expandable accordion section within the UI item, because...
* it would blur the lines between UI item and UI presentation table,
* there are already other elements like the comments that open a modal which provides an alternative,
* the quick choice user intent is built around immediate decisions. If the decision can't be made from what is already presented, it's likely that we are leaving this user intent and another view and/or UI component might be more fitting.

One of the use case for an expanding area was the list of preconditions. However, such a list is potentially very long and would interrupt the overview nature of the repository.

Useres that are missing the option to make hidden properties visible, are very likely managing users or administrators. For them [new Manage screens](https://docu.ilias.de/goto_docu_wiki_wpage_6969_1357.html) might be a more desireable option.

### Highlighting within a semantic group
Originally, we expected that an option to highlight properties within their group was needed functionality, like the legacy item was showing the Offline status in red.

However, since there are Primary and Secondary identifiers, the Main Identifier section, the Blocking Precondition and the Leading Property to highlight various properties for different reasons, there are plenty of opportunities to feature information prominently.

This is why we highly recommend formatting all information within a semantic group and priority area as similar as possible to create visually calm sections that step behind the featured areas. The order of the properties and different property types within one group may create a slight weighting (e.g. a property with an icon will stand out compared to a text).

## Possible objections and challenges
With a look at the ILIAS instance of the University of Bern and some demo instances from Concepts and Training GmbH we discovered that most of the changes outlined in this document are likely to only cause minimal shifts in 80-90% of the repository objects there. If an item only displays 1-2 properties besides the tile and icon, there is not much that could be impacted at all (unless we decide to change the base design of the UI item which is not currently planned).

This concept really shines in the extreme cases e.g. when a course is configured with all possible options and limitations (which is a considerable time investment for the managing user and therefor a bottleneck for the existance of such items). Only items that have it all at the same time (event date, registration date, availability information, learning progress, custom-meta etc.) are likely to show a drastically visible change, where some properties are highlighted more clearly and others step back more than in the legacy item.

We believe that this does a great sercive for the quick choice user intent that the average user is favoring most the time. However, we did notice some topics that might cause understandable concerns and want to address them in this section:

### Who sets the logic for the Priority Areas?
At first we were concerned, that the need to fill the Priority Areas with properties could pose an unfortunate amount of work on the maintainers of objects. However, we do believe that a very basic default logic might cover the needs of most cases already. Further logic would be set up as an exception on top of it.

This is an example for a possible default set up:
* Primary Identifier: Title
* Secondary Identifier: Icon
* Blocking precondition: Anything that actively prevents the average user from opening the object
* Leading Property: Not set

From this basic mapping, maintainers could set up conditions that fill the the Priority Areas differently or leave the default behavior and already have a decent information architecture in their item.

Providing suggestions for Leading Properties is a small project the paricipants of the workshop would be interested in doing.


### Won't jumping properties be distracting?
* Pulling properties to featured areas conditionally might cause them to appear in different places at different times.
* Properties loaded in a row might shift due to neighbouring properties being shown or hidden. Both might be percieved as restless when a long list of differently rendered items makes these shifts apparent.
* However, we do believe that such a flexible display of properties is welcomed by the average user.

For example, if a course is not accessible because all seats are taken, a user is likely to be frustrated to find this information burried in a list of equally presented availability properties.

As visually pleasing as it might be in theory to have a static order, the property keeping its default position and formatting is of no value in this case. The property jumping front and center into the Blocking Precondition area on the other hand addresses a possible confusion before it can even come up.

While there will be cases where this logic will make wrong assumptions about what is a very important property at a given time, **the benefits of matching the user's interest most of the time will make for a much smoother and frictionless user experience.**

A wrong assumption is further softened by the other Priority Areas. If the Blocking Precondition of the item wasn't what the user was looking for, the Leading Property presents a next probably relevant information prominently. If that assumption was also incorrect, all other properties are still rendered by descending priority.

So in the worst case, finding information is as overwhelming as it was in the legacy item and in the best case, users see what they were looking for immediately without questioning why it was positioned in a more prominent position.

### Do properties jumping in front of the title hurt accessibility?
In mockups we discovered that we wanted to pull properties to Priority Areas next to or above Main Identifiers because seeing users can read leading information and a subsequent title almost simultanously. However, people using screen readers are likely to expect some Main Identifiers being announced before even the most important properties.

Therefor the DOM structure of the UI item should probably reflect how screen readers should perceive the item and the order that people prefer when tabbing with the keyboard. We can then use CSS (flexbox and grid) to visually alter ans optimize the order for seeing users.

These accesibility considerations should be at the core of the html template used for this UI item. An unnested structure might also help frontend developers to re-design the item in their skins if they so chose, purely with modern CSS.


## Next steps

We are happy to take the discussion about these findings back into the larger community and would be excited to move on to the following steps and projects:

[ ] add to the many afforementioned Feature Requests how concepts from this proposal could help to move them along
[ ] collect suggestions for Leading Properties for each object type
[ ] investigate which properties could be rendered differently to reduce clutter (e.g. just showing the value instead of "key: value", if the value sufficiently implies the key)
[ ] complete more mockups to further explore and test how the information architecture of Semantic Groups and Priority Areas can best be translated into a visual design
[ ] create a UI repository item that supports the Semantic Groups and Priority Areas and offers hooks for dynamically pulling properties to Priotity Areas
[ ] replacing the legacy components in the repository list of objects

We also stumbled onto the folliwng topics that might be worth exploring further:

[ ] a sort by object type in the repository could show the object icon only once per type in a header instead of on every single icon to further decrease visual redundancy
[ ] the possible actions that can be triggered on an UI item are not yet categorized semantically and do not have a Priority Area like a call to action button (this could be useful to save some clicks e.g. join a course or confirm attendance from the outside)
[ ] the UI card might benefit from the exact same Semantic Groups and Priority Areas to the point where a width restricted item (e.g. on mobile screens) with a tile image as the Main Identifier might look very similar if not identical to a card.