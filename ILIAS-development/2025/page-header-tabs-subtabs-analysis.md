# Tabs and Subtabs Analysis & Optimization

Tabs and Sub-Tabs are one of the most prominent places for navigation in ILIAS. Through a bar in the header of a page, users can access different settings and contents.

At times, the tab navigation can be frustrating, because...
- when dozens of tabs fill the header, **finding a specific one is slow,**
- some tabs do **not contain what a new user would expect,**
- other buttons in or near the header offer similar or the same options, which can cause **confusion.**

Given that these tabs are such a central concept in ILIAS, we will use this paper to
- describe the existing use of Tabs and Sub-Tabs in ILIAS
- analyze strengths and weaknesses of tabs in general and ILIAS Tabs specifically
- explore strategies and structures that would help users navigate with less friction and more quickly

In the end, we arrive at concrete **recommendations on how to minimize frustrations** and optimize the user experience. The aim is to make ILIAS both **more accessible to beginners and quicker to use for power users**.

## Methodology

### Workshop

In July 2025, we conducted a one-day workshop at CaT Concepts and Training GmbH in Cologne with the following people contributing their expertise:

- Ferdinand Engländer, CaT Concepts and Training, Frontend Developer, ILIAS CSS authority for Code Changes
- Nils Haagen, CaT Concepts and Training, Developer
- Yvonne Seiler, University of Bern, Designer, ILIAS CSS authority for Conceptual Changes
- Denis Strassner, University of Hohenheim, ILIAS Test & Assessment authority for Conceptual Changes

In the workshop we...
- identified obstacles and inconsistencies that might confuse users
- experimented with alternative and refined structures to simplify and enhance tab navigation
- brainstormed how the new approaches would work in different areas of ILIAS

This paper builds and expands on the findings and ideas generated in this workshop.

### Building on the Knowledge of Pros

Furthermore, we will be referencing design best practices, studies and user testing results used by many professional designers and established projects. One important source are the publications of the [Nielsen Norman Group](https://www.nngroup.com).

## UI/UX Best Practices

First, let's establish how we can **measure if a tab UI is good or bad.** Having measurable indicators makes it easier to identify problems as well as measure if improvements are successfully reaching their goals.

### Time

"In most situations, the faster a user can complete a task, the better the experience."[^measureux01] **Both beginners and power users appreciate if they spend less time to reach a goal.**

[^measureux01]: Tom Tullis, Bill Albert. Measuring the User Experience. Morgan Kaufmann, Elsevier. 2nd edition. 2013. p. 74.

### Actions & Lostness

One of the best metric for a UI's effectiveness is measuring the number of user actions. "For websites, mouse clicks or page views are common actions".[^measureux02]

Each action requires physical and mental activity from a user, so lowering the number of total actions generally **feels better and less straining** to them.

The worst kind of action is one that didn't bring the user closer to the end of their task. Observing actions, we can estimate how lost a user has gotten. To calculate a lostness metric, researchers factor in (among other things) "The total number of pages visited while performing the task, counting revisits to the same page"[^measureux02] versus "The minimum (optimum) number of pages that must be visited to accomplish the task".[^measureux02]

[^measureux02]: Tullis. Measuring the User Experience. p. 87 - 88.

### The Will of the Users

To evaluate design choices we also need to focus on the perspective of a specific user doing a specific action using ILIAS. We can approach understanding the user better by approximating and examining...

* the **user intent**: "the purpose of a user’s series of actions" [^intro-user-graph]
* the **mental model**: "what users know (or think they know) about a system" [^nielsen_mental-models]

[^intro-user-graph]: Ciprian Borodescu. A gentle introduction to orchestrating intelligent journeys with User Intent Graphs. February 13, 2022 https://uxdesign.cc/a-gentle-introduction-to-orchestrating-intelligent-journeys-with-user-intent-graphs-503192a637e2 visited November 29, 2023.
[^nielsen_mental-models]: Jakob Nielsen. Mental Models. nngroup.com. October 17, 2010. https://www.nngroup.com/articles/mental-models/ visited November 29, 2023.

The interactive functionality of an UI element (or really anything) can be examined as its affordance:
* "an **affordance** is what a user can do with an object based on the user’s capabilities. [...] A door affords opening if you can reach the handle. For a toddler, the door does not afford opening [...]. [It's] an action possibility in the relation between user and an object."[^interaction-design_affordance]

[^interaction-design_affordance]: Interaction Design Foundation - IxDF. (2016, September 13). What are Affordances?. Interaction Design Foundation - IxDF. https://www.interaction-design.org/literature/topics/affordances visited December 5, 2023

## Current state

Across all screens we looked at for this paper we found the following types of Tabs and Sub-Tab entry:

- Navigating to a settings page for the current object:
- Navigating to content meant to be read, viewed or worked through:
- Navigating to a screen for creating or managing sub-objects:
- Navigating to a page to assign users to the current object:
- A back navigation that leads to a past screen:
- A back navigation that leads to an unexpected page:
- Starting an action that creates or changes data:

Furthermore, we found these same types of operations on other elements near the tab bar:

Toolbar

Top-right Dropdown

## Current issues

## 

Towards Semantically-Aware UI Design Tools: Design, Implementation and
Evaluation of Semantic Grouping Guidelines https://storage.googleapis.com/gweb-research2023-media/pubtools/7295.pdf

Nested Tab UI https://www.designmonks.co/blog/nested-tab-ui

Visual Hierarchy in UI: https://www.nngroup.com/articles/visual-hierarchy-ux-definition/

What are Gestalt Principles? https://www.uxdesigninstitute.com/blog/gestalt-principles-ux-ui-design/

Gestalt Proximity https://www.nngroup.com/articles/gestalt-proximity/
