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

### The Need of the Users

To evaluate design choices we also need to focus on the perspective of a specific user doing a specific action using ILIAS. We can approach understanding the user better by approximating and examining...

* the **user intent**: "the purpose of a user’s series of actions" [^intro-user-graph]
* the **mental model**: "what users know (or think they know) about a system" [^nielsen_mental-models]

[^intro-user-graph]: Ciprian Borodescu. A gentle introduction to orchestrating intelligent journeys with User Intent Graphs. February 13, 2022 https://uxdesign.cc/a-gentle-introduction-to-orchestrating-intelligent-journeys-with-user-intent-graphs-503192a637e2 visited November 29, 2023.
[^nielsen_mental-models]: Jakob Nielsen. Mental Models. nngroup.com. October 17, 2010. https://www.nngroup.com/articles/mental-models/ visited November 29, 2023.

The interactive functionality of an UI element (or really anything) can be examined as its affordance:
* "an **affordance** is what a user can do with an object based on the user’s capabilities. [...] A door affords opening if you can reach the handle. For a toddler, the door does not afford opening [...]. [It's] an action possibility in the relation between user and an object."[^interaction-design_affordance]

[^interaction-design_affordance]: Interaction Design Foundation - IxDF. (2016, September 13). What are Affordances?. Interaction Design Foundation - IxDF. https://www.interaction-design.org/literature/topics/affordances visited December 5, 2023

### Implementation Model

In this paper we will frequently be comparing the mental model with the implementation model.

> The implementation model represents how a system (application, service, interface, etc.) works. [...] It is shaped by technical, organizational, and business constraints.[^ux-mental-representation-implementation]

To make a system as complex as ILIAS work, it's built very modular with many services constantly interacting and reaching into each other. It's only logical that developers might build the UI around the structure of their implementation. 

Unfortunately, when we map processes that happen in the database or between services to the UI, views can quickly become overwhelming and crowded.

Taking an interface from average to great means simplifying it and "shielding" the user from the details of the implementation: "To book a flight from NYC to Zagreb, users don’t need to know everything in the background. They are, typically, exposed to simple forms – enter your destination, dates, and the number of passengers."[^ux-mental-representation-implementation] You can always expose more options and more information later when a user clearly indicated that they would like to have more control.

[^ux-mental-representation-implementation]: Vibor Cipan. 2020, September 27. UX mental model, implementation and represented models in UX. https://pointjupiter.com/ux-mental-model-representation-implementation-user-experience-development/ Ausgust 13th, 2025


### Memory for 7 +/- 2 chunks

"In 1956, [George A.] Miller found that most people can remember about 7 chunks of information in their short-term memory." This is a very important number to keep in mind when designing interfaces as it imposes a limit on what feels easy to process.

Another useful finding is that a single chunk can actually chunk together multiple pieces of information: "people could remember 7 individual letters, or 28 letters if they were grouped into 7 four-letter words." Here is a string of 28 numbers: 8251936382632834763512650253. Put in groups of four, it's much easier to process for the brain: 8251 9363 8263 2834 7635 1265 0253.

So grouping similar elements together can greatly reduce the mental effort required from seeing individual things. Instead the user now perceives manageable chunks.

## Current issues

### Number of Tabs

Going into the settings tab of any ILIAS Test & Assessment, a person with permission to edit sees (at the time of writing) 11 Tabs, 9 Sub-Tabs and there are 5 more options inside the action dropdown at the top right. While this is an extreme example, it illustrates how there is very little structure or limit that prevents objects and forms in ILIAS from continuously growing in number.

The 7 +/- 2 guideline mentioned earlier is broken and screens require the user to read every single tab's name to find the one that is actually relevant.

### No Hierarchy in Tabs of the same Bar

No tab label in their corresponding bar is visually different from another (except for the Back tab which shows a glyph). This is problematic, because not all tabs have the same relevance to the user at any given time. A general settings tab is much more frequented than some obscure advanced settings.

There is a light sense of priority given in their order: Tabs to the left are noticed first because of the left to right reading order. The rightmost entry is also likely to get more attention than an entry in the middle. Users tend to look for save buttons and important dropdowns in the right top corner of screens and groupings.

### Adaption to User Intent

Additionally, the tab bars do rarely anticipate or support the User Intent. With few exceptions they display all tabs that the current user has access to all the time. This means that even if a user is doing completely different tasks they are forced to see a lot of currently irrelevant elements.

However, over time or because of the role of the user within an institution, one user's tasks might be vastly different from another's. For example, in the case of the Test & Assessment maybe they want to...
- set up a simple multiple choice quiz for a quick evaluation at the end of an in person lesson
- set up a complex exam that hundreds of people will take and that needs to follow strict legal guidelines
- replace placeholder images in dozens of questions
- check in on a published test and see how many people have already completed their pass

Even if there are specialized screens for some of those activities, we do not simplify or optimize the page header. The user generally has to set and find their own focus and disregard (in some cases) dozens of elements irrelevant to their current task.

We do already adapt to one User Intent relatively well:
- A user with only the permission to take the test, actually sees a highly minimized interface with fewer to even no tabs.

This reduction feels fantastic for someone who just wants to focus on the Test questions being put before them. This is how an article on UXmatters.com describes the best case scenario:
> "If you understand users’ needs, you can ensure that you’re communicating the right message to users, through the right medium, at the right time." [^uxmatters-user-intent]

[^uxmatters-user-intent]: Jordan Julien. The Importance of Knowing User Intent. uxmatters.com. October 22, 2012. https://www.uxmatters.com/mt/archives/2012/10/the-importance-of-knowing-user-intent.php visited August 13th, 2025.

The relief a test participant feels when thrown into a very focused view is something we could bring to more areas of ILIAS - even to administrators, because they too might appreciate tunnel vision for some tasks.

Therefore, we want to explore how we can organize and build views more around very specific, focused user intents. A direct reflection of such a re-structuring will be how we treat Tabs and Sub-Tabs.

## Analysis of the current State

To further examine the Tabs & Sub-Tabs across various screens, we need to examine their current function and purpose. Sometimes, entries presented within the dropdown menu and toolbar also perform the same way as some tabs. Therefor, we include them in this evaluation.

### Scope of examination

We focused on the following areas of ILIAS:

- Test & Assessment
- Question
- Course
- Administration > System Settings > General Settings
- Administration > Repository & Objects > Repository
- Administration > Repository & Objects > Study Programme
- Category
- ILIAS Learning Module
- Wiki

Let's start by identifying the different types of Tabs. Here is a screenshot of the Test & Assessment during question creation:

![Test-in-ILIAS-10.png](imgs/Test-in-ILIAS-10.png)

After some brainstorming during the workshop that this paper is based on, we landed on the following categories:
- Settings of this object: Settings, General, Grading System, Permissions
- View/Work-Through Content: Test
- View/Work-Through Reports: My Result
- Create content: Edit introduction
- Manage/create sub-objects: Questions, Export
- Connect this object with other objects: Participants

We also found...
- Navigation Back or Up

### Developer vs User Perspective

We realized we needed to clarify some of these terms, because in this paper we aim at what the user understands things to be, not at how they are actually programmed:

- The term "object" is clear when the user opened a repository object (a Test, a Course, a Category). However, there are contexts the user perceives as object-like contexts despite them not being a full objects in the eyes of a developer (e.g. the Calendar or Contacts Screen). Because our focus is on UX, we call any context that the user might feel like they are inside an "object" as such (comparable to a physical Calendar or an Address Book). On the other hand, Learning Progress is technically an object, but the User is likely to see it as an attribute of the main object, not even a sub-object. Therefore, we count anything Learning Progress related either as a View or a Setting of the object itself.
- The term "sub-objects" means items the user creates seemingly as part of the main object. These items are usually a repeating group for the same kind of information and often have their own settings. More simple items like comments are referring directly to the main object and belong to it despite them being something separate and more general inside the code of ILIAS. Similarly, Questions can technically exist somewhat outside a Test, but once they are inside a Test or Pool, no user would see them as independent objects.
- "Create content" describes the creation of one body of content. In this case the user doesn't feel like they are creating a collection of items (even if it's technically what they might be doing e.g. with the blocks of the Page Editor). They think that they are filling one specific location or one set of fields to be shown to the consumer.
- "Connect this object with other objects" refers to connecting two objects a non-programmer User may strongly perceive as separate. This is mainly true for things the user is very aware of existing in multiple places e.g. adding Members to a Course or Participants to a Test. 
- "View/Work-Through Contents" describes a body or collection of content made by one user to be consumed and interacted with by another. The consumer may fill out or provide input, but they do not change the content itself.

The goal with these distinctions is to meet the user's mental models. To reduce friction in the UX, we have to optimize for how users instinctively think the interface and the objects work, not for how they actually work.

### Measuring the status quo

We had a look at 20 screens. As one screen we define the view a user sees when entering an object. Usually within one screen the Tab bar stays the same and Sub-Tabs change depending on the currently selected Tab.

When advancing through Tabs to evaluate Sub-Tabs, the main Tabs have not been counted again. However, entries with the same name and behavior that are repeated on different screens are counted as separate occurrences.

|                           | Tabs | Sub-Tabs | Toolbar | Top-Right Dropdown |
|---------------------------|------|----------|---------|--------------------|
| View/Work-Through Content | 26   | 3        | 11      | 1                  |
| View/Work-Through Reports | 4    | 9        |         |                    |
| Manage Sub-Objects        | 35   | 16       | 1       |                    |
| Create Content            | 4    | 7        | 17      | 6                  |
| Connect Objects           | 5    | 2        |         | 2                  |
| Settings of this Object   | 53   | 13       | 2       |                    |
| Actions                   | 2    | 3        | 26      | 5                  |
| Navigation back or up     | 8    |          |         |                    |

### Noteworthy observations

#### Inside Out Settings

We looked at 20 screens. Almost every screen has a Tab named "Settings" that branches into Sub-Tabs for various categories of settings. However, we counted 53 occurrences of a Tab leading to "Settings of this Object".

This means that some settings an average user understands to be part of the object are not under the "Settings" Tab. Most notable are the Learning Progress and Permission Settings which have their own main Tab. Non-techy users understand these to be attributes of the current object just like its online status.

This order might have been chosen because it resembles more closely what is happening under the hood of ILIAS. Learning Progress and Permissions are 


Most non-techy users understand these to be attributes of the current object just like its online status.

This structure assumes that Learning Progress and Permissions are so important that they need to be Tabs instead of a settings Sub-Tab.

## 

Odd places:
- Kursmitgliedschaft beenden
- Info in Dropdown Lernmdoul

Towards Semantically-Aware UI Design Tools: Design, Implementation and
Evaluation of Semantic Grouping Guidelines https://storage.googleapis.com/gweb-research2023-media/pubtools/7295.pdf

Nested Tab UI https://www.designmonks.co/blog/nested-tab-ui

Visual Hierarchy in UI: https://www.nngroup.com/articles/visual-hierarchy-ux-definition/

What are Gestalt Principles? https://www.uxdesigninstitute.com/blog/gestalt-principles-ux-ui-design/

Gestalt Proximity https://www.nngroup.com/articles/gestalt-proximity/
