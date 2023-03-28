# Delos Refactoring Projects

Now that Delos has been moved to the ITCSS SCSS codebase the following projects focus on making the creation of System Style skins easier.

## Skin Repo

* Complete setting up the ILIAS repo to Custom System Style Skin Repo automation
* Start documentation on how this repo is supposed to be used

## Naming Convention for Settings Layer

* at least in the settings layer the variables should have BEMIT names
* "text" or "background" are sometimes omitted from variable names. That could cause confusion, so `il-btn-primary-color` should be `il-btn--primary__text__color` to be absolutely clear.

## Clarify scope of color variables

* e.g. gray color il-neutral is sometimes used to directly change text or border colors
* this makes creating accessible light or dark skins difficult
* text colors should use variables meant for text, border colors should use variables meant for borders - these location specific variables should be filled from general color palettes, so a skin can decide to keep or break this connection 
* general palette vs. pattern palette (borders) vs. specific location palette
    * Are 3 layers desired? E.g. `$il-highlight-bg in general palette` > `$il-menu-entry--hover__bg: $il-highlight-bg` > `c-dropdown__item--hover__bg: $il-menu-entry--hover__bg`
    * Where do we place pattern palettes?

## Grayscale Revision

* some grayscale variables are called neutral-color, some have a main-dark-bg namespace
* maybe naming and purpose could be clarified?
* maybe stricter chain of general palette (dark, darker) to pattern (zebra-odd, zebra-even) to specific location (calendar rows)

## Consistent typography system

* Currently typography settings are mashed together from Bootstrap, Delos specific overwrites and side effects from elements that actually shouldn't effect the base typography (p margins are styled together with ul, ol)
* we should either 100% consistently use the very well thought out typography system from Bootstrap exactly as they intended (ideally updated to version 5) or completely define our own system
* focus point 1: text sizes
* focus point 2: margins (do we work with margin-top or -bottom, cutting first-/last-child margin?)
* focus point 3: checking if browser zoom and other accessibility tools transform text as expected

## Spacing Variables

* it's not really clear when to use xlarge, xxlarge or xxxlarge spacings
* the spacings base, small and xs are tiny - increments of 3 px are not really readable as distinguished steps in spacing

## Completing the set of variables for clickable elements

* clickable elements do not have the complete set of variables exposed to create very unqique styles e.g. links do not have a text-decoration variable
* we probably need the following variable groups:
  * text links (e.g. links in page paragraph)
  * navigation links (e.g. breadcrumbs, text that reads as clickable because it's never ever part of a paragraph)
  * drop menu entries
  * buttons
    * --standard
    * --primary
    * --viewcontrol
    * --bulky
    * --bulky--link
  * accordion head
  * tree item
* each variable group includes at minimum
  * x__text/bg/border__color
  * x--hover__text/bg/border__color
  * x__border__radius/width/type
  * x--hover__border__radius/width/type
* they may include
  * x__text__decoration
  * x--disabled__text/bg/border__color
  * x__icon/glyph/toggle__color
  * x__icon/glyph/toggle__position
  * x__icon/glyph/toggle__display
  * x__min-height
  * x__padding

## Add missing variables for mainbar/slate

* not all colors in the mainbar or slate can be changed or inverted through variables, causing the need for complex and fragil patches in some system style skins
* all colors should be accessible through variables, glyph colors should be easier to invert

## Refactoring Presentation Table to use flexbox layout

* There are problems with the action dropdwon/button being overlapped by content/header. These have been patched, but a flexbox layout could be a more durable solution
* Flexbox layout will enable service providers to tweak the appearance of the presentation table to the needs of their customers

## Text white vs inverted

* setting colors to white (the value, not a variable) makes it very difficult to create very light or no-background-fill skins
* instead $il-text-color-invert should be used (and maybe a set of 2-3 inverted backgrounds)
