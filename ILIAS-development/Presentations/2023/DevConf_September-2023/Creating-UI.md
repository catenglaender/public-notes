---
marp: true
---

Call for papers




# What UI do users, designers and frontend developers really want?

How do good UI and style-code make users, designers and frontend developers happy? ILIAS 9 comes with some new, some re-factored and some visually improved UI Components to offer more frictionless user experiences and a highly manageable code base.

After many lessons learned in development, we share best practices, checklists and solutions that anyone working with style code in ILIAS 9 might find useful.


---

# What the user always wanted

Creating intuitive concepts and efficient style code for UI components

---

Recent experiences from working on ILIAS 9 UI:

* What are good UI choices?
* Is strict structure a curse or a blessing?
* What chances does removing a dependency bring?

---

Examples we will discuss

* Data Table
* Mode Info
* View Control Mode

---

## Making good UI choices

---

Sadly, no mind control interface for ILIAS yet.

---

No one wants to make bad UI choices.

But bad UI choices happen, because of reasons.

---

Good or bad for which user exactly?

---

### User Intent

---

### Mental Model

---

### Examples

---

Sticky Header for Data Table

* keeping in view what the user needs to see

---

View Control Mode Info

* engaged state wasn't clear with just two buttons

---

## Curse and Blessing of Structure

---

New SCSS Coding Guidelines

---

### ITCSS & SASS

---

blessing

* everything has a dedicated place

---

curse (blessing in disguise?)

* some choices are hard to make
* some legacy code barely fits
* SASS is very strict

---

### Naming Convention

---

### Variables

from Settings to Mixin to Components to local

---

## Example

Let's re-factor and re-design the Mode Info

---