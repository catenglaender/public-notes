---
theme : "white"
transition: "slide"
highlightTheme: "monokai"
logoImg: "./img/logo.png"
slideNumber: false
title: "Item Properties - UX Principles"
---

# Object Properties - bringing order to chaos

---

## The challenge

---

### So many properties on an object

---

![Image of an item with many properties](img/item-with-many-properties.jpg)

---

* the title
* a description
* a variety of dates and deadlines
* icons
* a learning progress
* tags
* comments
* previews
* and much more...

---

Properties can pile up...

...so let's try grouping and sorting...

...and see what changes.

---

### Example 1: ???

![Example 1](img/example-01.jpg)

---

### Example 2: ???

![Example 2](img/example-02.jpg)

---

### Example 3: ???

![Example 3](img/example-03.jpg)

---

### Minimal items barely change

Grouping doesn't change much for elements with little properties

![Example 4](img/example-04.jpg)

---

## The approach to find groupings

---

What is the system behind the example groupings?

---

### Considering User Intent

* most of the time the user is not an admin, but a learner

---

* admin: wants to see all properties for managing and sorting
* normal user (learner): trying to find something quickly

---

[UX Guide for Repository Object Properties](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/src/UI/docu/ux-guide-repository-objects-properties-and-actions.md)

General User Intents

* Making a quick pick
* Managing multiple objects

---

#### Making a quick pick

* one clear choice for one expected object
* glancing at one or two of its properties
* action shown as the most prominent usually the reason why user came to this view


---

### Existing collections of possible properties

* Very helpful table in FR [Streamline Object Properties](https://docu.ilias.de/goto_docu_wiki_wpage_7399_1357.html)

---

### Property Types vs Semantic Group

* Type: Date
* Possibly different Semantic Groups:
    * Event Date
    * Registration
    * Availability
    * Deadline 

---

### Semantic Groups

* same kind of information close together
* user learns default order and position

---

### Priority Areas

* make important information jump out visually
* e.g. user can't open a course, would immediately like to know why
* really quick decisions become possible

---

## Workshop

---

### Finding the Semantic Groups

---

### Testing with Mockups

---

### Feedback and Tweaking

---

## Result: Semantic Groups

* Main Identifiers (title, tile image, icon, event date)
* Personal Status (learning progress, membership)
* Availability (availibility time frame, seats left)
* Main Descriptors (description)
* Reactions (comments, star-rating)
* Generated Meta-Data (creation date, file type and size)
* Custom Meta-Data and Legacy

---

## Result Priority Areas

Filled from the Main Identifier Group:

* Primary Identifier (title)
* Secondary Identifier (icon)

---

Filled from the Availability Group: 

* Blocking Preconditions (explain access restriction)

---

Filled from Reactions:

* Prioritized Reaction (comments might be more important than the star rating)

---

Filled from any group:

* Leading Properties (learning progress is important for follow-up visits)

---

### Leading Properties

* anticipating main user intent is now possible
* there are good reasons for it, but not mandatory
* exact logic has to be developed case by case

---

## Coding

* right now all properties are dumped into "withProperties"

---

* in the future properties could be sorted into the different groups
    * withGroupMainIdentifiers
    * withGroupPersonalStatus
    * withGroupAvailability
    * withGroupMainDescriptors
    * withGroupReaction
    * withGroupGeneratedMeta
    * withGroupLegacy

---

* and additionally priority areas can be filled by marking specific properties (just and example, implementation details are yt to be determined)

```PHP
$crs_item = f('title', 'icon') //define primary and secondary identifier during construction
    ->inGroupPersonalStatus('progress', 'membership')
        ->withLeadingProperty('progress')
    ->withAvailibility('date', 'permissions', 'preconditions')
        ->withBlockingCondition('precondition')
```

---

### Sortierung eröffnet Möglichkeiten

---

## Outlook

Repository object MUST be replaced by UI item soon

---

## Possible new look
