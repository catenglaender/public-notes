# Proposal for a semantic Button and Link Type Hierarchy

## Goal

Currently, **buttons and links are styled inconsistently in ILIAS.** For example, sometimes "Add New" is a Primary Button, on other pages it is a Default Button. In some places, tables are accompanied by View Control Buttons, in others the same options are presented as Shy Buttons.

With this proposal we want to create a framework to bring consistency into this chaos.

Consistent hierarchy and reliable behavior will help both beginners and experienced users to **navigate more quickly and frictionless** through our interface.

## Proposal



## Buttons vs. Links

An article on makethingsaccessible.com puts it plain and simple:
* "A link goes somewhere,
* a button does something" [^makethingsaccessible-link-button-def]

[^makethingsaccessible-link-button-def]: Darren Lee. Links vs buttons vs other clicky things. April 16, 2023. makethingsaccessible.com. https://www.makethingsaccessible.com/guides/links-vs-buttons-vs-other-clicky-things/ visited on January 21, 2026

There are two sides to this:
* users already expect them to look a certain way
  * links are underlined text
  * buttons are padded boxes
* they have different functionality
  * Links may show the target URL in the browser and cause a page reload. The keyboard shortcut to open them is ENTER
  * Buttons generally do not cause a reload. Keyboard shortcuts to interact with them is ENTER and SPACEBAR. They are announced by screen readers as "push buttons"

Not following these standards will break the users mental model of how they expect things to work. And that is never not good. It confuses and overwhelms users.[^breaking-mental-models-examples]

[^breaking-mental-models-examples]: Jason Clauss. BUXRU #24: This is what happens when you break the mental model. December 6, 2018. uxplanet.org. https://uxplanet.org/buxru-24-this-is-what-happens-when-you-break-the-mental-model-ffbce96cccea visited on January 21, 2026

## Two Dimensions

We need to look at two factors that seem to guide the styling of links and buttons:

* Information Architecture Hierarchy: How relevant or consequential is the action?
* The Semantic Type: What type of action will be triggered?

### Information Architecture

Typically, many webapps seem to use three visual levels of priority for their **buttons**:

* primary
* secondary
* standard

Arguably, there often is one more visual level below the default: Shy buttons. Those buttons look like links but are technically still buttons. Otherwise, buttons are often above links in the Information Architecture.

**Links** within a system usually borrow their base style from the surrounding text. This means they also take over a similar priority within the information architecture. A body link stands out just slightly from the body text. A headline link might be equal or slightly above the information layer of the headline it is in.

However, just like with the buttons, there is one common case to break this pattern: Many Call-To-Action buttons used in modern web interfaces are not actually buttons. They lead away from the current page so they are technically links, but visually look like buttons.

Except for this quirk where buttons and links visually look like their counterpart and for very large clickable headlines, buttons are generally more attention grabbing than links.

Let's summarize the hierarchy that this gives us from most to least attention-grabbing:

* links in large headlines
* button primary (and Call-To-Action Links looking like it)
* button secondary (and Call-To-Action Links looking like it)
* button standard (and Call-To-Action Links looking like it)
* links in text (and buttons looking like it)

This is a purely visual hierarchy. With this framework, **we know that a Button primary is more eye-catching, but so far we do not know when a Button should be a Button Primary.** We need a second criteria for making these decisions.


