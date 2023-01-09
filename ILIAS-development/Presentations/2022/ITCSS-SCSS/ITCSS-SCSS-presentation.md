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

## ITCSS structure

1. settings
2. dependencies
3. tools
4. normalize
5. layout
6. elements
7. components
8. hacks and tweaks

---

Original proposal: https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/src/UI/docu/sass-guidelines.md

---

### 1. Settings

very general settings like

* main colors
* logo size
* button primary color
* main border color, width, radius
* header height

---

tendency: less general variables should influence most components in the same way

---

e.g. `$ui-panel-border`, `$ui-item-seperator`, hr

should all use `$il-main-border-color` and `$il-main-border-width`

---

not good: 3 unrelated components use `il-card-border-color`

---

### 2. Dependencies

* SCSS files from dependencies
* modified SCSS files from dependencies
* additions to dependencies

---

### 3. Tools

Mixins & functions

* Pixel to rem conversion
* Focus
* Generation of color shades

---

### 4. Normalize

* Remove browser specific styling (Bootstrap)
* some baseline settings (like loading fonts)

---

### 5. Layout

* Positioning and spacing of components in relation to other components
* Spacing variables
* Standardpage variables that aren't settings

---

### 6. Elements

* basic styling of all unclassed HTML-elements
* Bootstrap is doing a lot of this

---

### 7. Components

* UI components
* Legacy components
* Delos code belonging to a group that can be seen as a component

---

### 8. Hacks and Tweaks

* should be empty
* still used?
* should be solved differently

---

### Advantages

* encourages looking into higher layers for variables
* code that belongs together is contained together
* better overview, easier refactoring

---

Code Guidelines WIP: https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/templates/Guidelines_SCSS-Coding.md

---

Rules and structure will probably still evolve over time

---

### Replacing Bootstrap 3

* proposal: pulling from libraries instead of framework base

---

* replacing / ingestion not far in PR yet
* will be easier because all code to refactor for a component is ideally in two places only:
    * e.g. buttons: Boostrap `_buttons.scss` and ILIAS UI `_ui-component_button.scss`

---

Future projects like:

#### Refactor button style code

---

* get inspiration from button we like (Bootstrap 5? Tailwind?)
* write our own and/or copy the parts we like into our UI component (or use a dependency if we find the perfect one)
* delete Bootstrap 3 button code

---

## Other possible projects

---

### Refactoring legacy modules and services

* local import at beginning of file reveals connections
* out of place classes are more obvious
* example: Course Module style code

---

### Box Shadow Concept

---

### Small Screen Breakpoints

---

### Flex-box and grid tools

---

### Hack and Tweak layer?

```SCSS
.ilCenter {
  text-align: center;
}
```

---

### Legacy Settings

---

### Switch to semantic classes

---

instead of

```SCSS
.ilCenter {
  text-align: center;
}
```

```HTML
<div class="my-component-header ilCenter">Component Header Content</div>
```

---

Mixins

```SCSS
@mixin ilCenterHeader {
  text-align: center;
  font-size: $il-font-size-h2;
}

.c-my-component__header {
  @include ilCenterHeader;
  ...
}
```

```HTML
<div class="c-my-component__header">Component Header Content</div>
```

---

Extends

```SCSS
%ilCenterHeader {
  text-align: center;
  font-size: $il-font-size-h2;
}

.c-my-component__header {
  @extend ilCenterHeader;
  ...
}

.c-another-component__alert {
  @extend ilCenterHeader;
  ...
}
```

```CSS
.c-my-component__header, .c-another-component__alert {
  text-align: center;
  font-size: 1.8rem;
}
```

---

## SCSS

---

* many modern frameworks use it (Bootstrap 5)
* easier to take inspiration from these frameworks
* SCSS has weekly updates, active development

---

* Dart SASS
* less2scss converter on npm

---

@while, @each, @for, @if, @else

---

@functions with @return

---

@warn, @error, @debug

a11y checks could @warn

Warning: Contrast between panel color and panel bg color is lower than 60%.

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

### Import

---

LESS
* @import "file"
* loads everything into one big file
* loops through it to replace values from variables again and again

---

SCSS
* partials with prefix `_` are never compiled on their own, have to be included by anotehr file
* @import is deprecated instead: @use "file"
* variables are locally solved on import within that file only

---

@use "folder"

looks for an _index.scss in that folder

---

A SCSS file needs to specifically be introduced to every other file it has to know variables from

---

Easier to see what other files and variables a file is depending on

---

### Variables

$ instead of @

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

LESS: last definition changes value everywhere

SCSS: new definition changes value from there on, previous uses stay the same

---

Definition with !default:

```SCSS
$padding-horizontal-sm: 3px !default;
$padding-horizontal-sm: $il-padding-horizontal-sm;
$padding-horizontal-sm: 3px !default; // is ignored
```

---

This allows:
* load unmodified bootstrap variables with default values
* load our re-definition of bootstrap variables
* load unmodified bootstrap variables again, re-defined variables persist, calculations mixing re-defined and default variables are done correctly

---

```SCSS
// bootstrap variables 1st load
$padding-horizontal-sm: 3px !default;
$navbar-btn-padding-right: $padding-horizontal-sm * 2;

// our redefinition
$padding-horizontal-sm: $il-padding-horizontal-sm;

// bootstrap variables 2nd load now using correct value
$padding-horizontal-sm: 3px !default; // default is ignored now
$navbar-btn-padding-right: $padding-horizontal-sm * 2;
```

---

There are other ways to do this...

@use "bootstrap/variables" with ()...

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

## Next steps

* Feedback
* more experiences
* tackle already mentioned projects
