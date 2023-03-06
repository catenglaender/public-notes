# ILIAS 8 looks like this

(screenshot delos_ILIAS-8.png)

---

# ILIAS 9 looks like this

(screenshots delos_ILIAS-9.png)

---

What's the difference?

---

* switched CSS pre-processor from LESS to SASS
* new structure of style code = ITCSS

---

# What is SASS?

* CSS Pre-processor to turn SCSS code into CSS
* has many functions that CSS doesn't (nesting)

---

# Why SASS instead of LESS?

* we couldn't update Bootstrap 3 for years because they switched
* many modern frameworks with useful concepts use SASS
* more possibilities e.g. more strict includes/namespaces, dictionary maps, if, each, functions
* automatic checks and testing with warning and debug messages

---

# What is ITCSS?

* file and folder structure
* sorted from most global to most local

---

# Why ITCSS?

* style code got a bit overwhelming and out of order in places
* we need more criterias to check quality of PRs

---

# ITCSS Structure

Detailed Documentation: trunk/templates/Guidelines_SCSS-Coding.md

1. settings
2. dependencies
3. tools
4. normalize
5. layout
6. elements
7. components
8. hacks and tweaks

---

Most important for many contributions:

1. settings
5. layout
7. components

---

# ILIAS 8

(screenshot Style-Code_ILIAS-8.png)

---

# ILIAS 9

(screenshot Style-Code_ILIAS-9_editLink.png)

---

# New naming convention

* for new CSS classes and SCSS variables
* Block, Element, Modifier = BEM + ITCSS = BEMIT

---

# Impact for making/updating System Styles

* you will need Dart SASS to compile the stylesheet
* 7 and 8 System Styles will be incompatible
* building System Styles through GUI remains an option (WIP)
* Skin Repository will make creating complex System Styles easier (WIP)