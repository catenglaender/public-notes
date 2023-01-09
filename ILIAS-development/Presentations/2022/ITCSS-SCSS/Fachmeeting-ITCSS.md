---
theme : "white"
transition: "slide"
highlightTheme: "monokai"
logoImg: "./img/logo.png"
slideNumber: false
title: "Item Properties - UX Principles"
---

# ITCSS / SCSS

---

* Vorstellung von Sass/SCSS
* Warum wir beim Skin-Bauen umdenken müssen
* ITCSS Struktur
* Ansatz für zukünftige Skins

---

Vorwissen: Warum benutzen wir einen CSS Preprocessor?

---

## Variablen

* Browser Support und Operationen mit CSS eigenen Variablen sind noch eingeschränkt
* Variablen machen das cate Pink zum LVM Grün

---

## Mixins

* Blöcke für wiederverwendbaren Code
* Parameter möglich

---

```LESS
.make-panel(@bg-color) {
    margin-bottom: @spacing-medium;
    border: @default-border;
    background-color: @bg-color;
    padding: @spacing-medium;
}

.my-new-panel {
    .make-panel(@bg-light);
}
```

---

## Sass / SCSS

---

* Sass ist der Name des Preprocessors
* SCSS ist eine mögliche Syntax

---

Why switch from Less to Sass?

* many modern frameworks use it (Bootstrap 5)
* easier to take inspiration from these frameworks
* Sass has weekly updates, active development

---

* Dart SASS 1.56.1
* less2scss converter on npm

---

@while, @each, @for, @if, @else

---

@functions with @return

---

@warn, @error, @debug

a11y checks could @warn

e.g. "Warning: Contrast between panel color and panel bg color is lower than 60%."

---

Dictionary maps

```SCSS
$color: (
  "main": blue,
  "secondary": green,
  "light-bg": gray);

$header-bg: map.get($color, "main");
```

---

### Variables

---

LESS: last definition changes value everywhere

SCSS: new definition changes value from there on, previous uses stay the same

---

$ instead of @

---

### Import

---

LESS
* @import "file"
* loads everything into one big file
* loops through it to replace values from variables again and again

---

SCSS
* partials with prefix `_` are never compiled on their own, have to be included by another file
* @import is deprecated instead: @use "file"
* variables are locally solved on import within that file only

---

Sass/SCSS compiles very fast. Less needed 10 - 30 seconds for some skins.

---

A SCSS file needs to specifically be introduced to every other file it has to know variables from

---

Challenge: How do we sneak variables in for creating new skins

---

Easier to see what other files and variables a file is depending on

---

variables are local to the file

unless other files are specifically making them usable

---

variables from @use are namespaced by default

```SCSS
@use "colors"; // imports _colors.scss

.class {
  background-color: colors.$il-main-color;
}
```

---

```SCSS
@use "colors" as col;

.class {
  background-color: col.$il-main-color;
}
```

---

```SCSS
@use "colors" as *;

.class {
  background-color: $il-main-color;
}
```

---

use with as * is currently used a lot

causes no conflicts because variables were global

---

in the future we should use namespaces so we see immediately where variables, mixins and functions came from

```SCSS
.class {
  background-color: settings.$il-main-color;
}
.class {
  background-color: tool-col-shades.light-shade-2(settings.$il-main-color);
}
```

---

Possibility to override Variables on import of a partial

```SCSS
@use "colors" as * with (
  $il-main-color: red,
  $il-main-border-color: black
);

.class {
  background-color: $il-main-color;
}
```

---

Definition with !default:

```SCSS
$padding-horizontal-sm: 3px !default;
$padding-horizontal-sm: $il-padding-horizontal-sm;
$padding-horizontal-sm: 3px !default; // is ignored
```

---

## The future has tools

Example: Pixel to rem conversion

---

```SCSS
@use "sass:math";
//** Used to calculate pixel to rem
$il-pixel-to-rem: 0.0625;

@function pixel-to-rem($convert-this, $conversion-factor: $il-pixel-to-rem)  {
    @if math.unit($convert-this) == "px" {
        $converted: math.div($convert-this,1px) * $conversion-factor * 1rem;
        @return($converted);
    }
    @else {
        @error "Pixel to rem conversion requires a pixel value as an input. Unit was '#{math.unit($convert-this)}' instead.";
    }
}

@function rem-to-pixel($convert-this, $conversion-factor: $il-pixel-to-rem)  {
    @if math.unit($convert-this) == "rem" {
        $converted: math.div(math.div($convert-this,1rem),$conversion-factor) * 1px;
        $converted: math.round($converted);
        @return($converted);
    }
    @else {
        @error "Rem to pixel conversion requires a rem value as an input. Unit was '#{math.unit($convert-this)}' instead.";
    }
}

@debug "20px in rem is #{pixel-to-rem(20px)}";
@debug "1rem in px is #{rem-to-pixel(1rem)}";
```

---

# ITCSS Structure

1. settings
2. dependencies
3. tools
4. normalize
5. layout
6. elements
7. components
8. hacks and tweaks

---

Code Guidelines WIP: https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/templates/Guidelines_SCSS-Coding.md

---

Why did we do all this?
* Clear funnel from broad to specific
...

---

* Easier to start writing new components

---

* Easier to refactor (just grab a file)

---

*  More mature coding possibilities

---

Wie bauen wir zukünftig Skins?

---

* Imports nutzen relative Pfade -> Kopieren von Delos

---

* Wie behalten wir den Überblick?

---

* Default Delos vs. System Skin

---

* Daniels Skin Repo Automatisierung macht aus den Kern Dateien einen System Style

---

* Diesen System Style forken wir und bauen ihn zu cate um

---

* Cate ist ein Basis Skin, kompiliert Kunden Stil Variationen