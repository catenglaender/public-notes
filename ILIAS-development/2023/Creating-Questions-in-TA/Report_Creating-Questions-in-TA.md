# Report: Creating Question (ILIAS Test & Assessment)

The ILIAS Test & Assessment is a core feature for many institutions and businesses that use ILIAS to train and evaluate students, employees and other learners.

ILIAS offers many different types of questions and a lot of options to create complex tests uniquely tailored to individual needs. The downside of such a powerful feature set is that navigating through many settings and views can be overwhelming and time consuming.

In this report we analyze the current state of the question creation process and make suggestions on how to make it more intuitive and efficient.

## User feedback

An E-Assesment conducted by ILIAS NRW among teaching staff of universities with 326 evaluated submissions gives us good insights on how the Test & Assessment Center is currently perceived (Report and Presentation in German): https://www.ilias.nrw/goto.php?target=cat_212

Here are some user voices from the report PDF report highlighting room for optimization with regards to question creation (English translation has been added):
* "Die Erstellung von Lückentextfragen ist nicht sehr benutzerfreundlich." (p. 22) / "The creation of Cloze Questions is not very user friendly."
* "Anlegen der [Single Choice] Frage recht kompliziert." (p. 23) / "Creation of Single Choice questions is quite complicated."
* "Der Editor ist sehr hakelig (gilt für alle Fragetypen)." (p. 28) / "The editor is very finicky (all question types)."
* "Zu aufwändig zu nutzen, alle Tests in ILIAS." (p. 28) / "Requires too much effort to use, all Tests in ILIAS."

One of the recommendation of the report is that the offered information material and support could be extended (p. 26). However, as this paper will demonstrate, there might be many issues we could solve with a more self-explanatory, intuitive interface design.

## General discontent

The voices we are more interested in for this paper, are the ones that claim the ILIAS Test & Assessment is "complicated" or requires "too much effort" in general.

Complaints about details can be made into feature requests or issue reports, but a general discontent is much harder to address.

To get behind how we could improve the user's general satisfaction we will
* use the amount of clicks and page loads as a measurable metric for friction in the interface
* look for UI/UX principles helping us to put issues and solutions into clear words
* analyze why creating questions in other quiz builder tools feels more effortless
* draw conclusions and make recommendations for how to improve the creation of questions in ILIAS

## Every click matters

When looking at other tools that allow creating questions for an interactive test or quiz, it's striking that ILIAS requires both the most amount of clicks and most amount times the interface replaces most of its content (e.g. shows a new view or tab).

In this table below we counted clicks and view changes when

* starting on the overview screen of an empty test or quiz
* creating one single choice true/false question,
* creating one multiple choice question with four options,
* assigning 10 points to the correct answers,
* ending on the overview screen


| Tool           | Click Count | Change of View | Set 10 points for correct answers |
| -------------- | ----------- | -------------- | --------------------------------- |
| ILIAS          | 31          | 8              | possible                          |
| typeform       | 19          | 3              | possible                          |
| quiz-maker.com | 18          | 3              | possible                          |
| H5P            | 16          | 0              | not possible                      |

H5P misses a feature to assign custom point values to correct answers (if it did it would probably require 20 clicks in total).

Quiz-Maker and Typeform have true/false or yes/no as a default option for a question with two choices. This saves 2 clicks as they didn't need to be changed. 

We only looked at the most simple question types as these are the most comparable across all the apps.

While a high click count is not necessarily frustrating for the user, replacing the entire view 8 times (complete page loads in the case of ILIAS) does demand a short re-orientation that can be mentally taxing and break the flow of work if it adds up for dozens of questions.

Going rapidly back and forth between the same views with a full page load is especially noticeable as UX designer Jared Spool concludes in [this article.](https://articles.centercentre.com/refresh-or-not/)

## Helpful UI/UX principles

Fortunately, we can turn to established UI and UX guidelines that have proven useful to improve the usability of software:

### User Intent

Knowing what precisely a user wants to do in any given view helps us to support them more accurately by showing the elements they are likely looking for more prominently.

The challenge during test creation is that the user's needs may change depending on their current focus.

### Mental Model

Users bring expectations of how an interface should work. These mental models are shaped by interfaces from other apps that they have used before.

In the E-Assessment by ILIAS NRW some participants mention interfaces they like more (H5P and even some specific question types) and criticize broken drag and drop functionality because previously shaped mental models.

### Miller's Law

Miller’s Law states that the immediate memory capacity of people is limited to approximately seven items, plus or minus two. Interestingly, single items can be grouped into chunks which are then seen as one item (which is why 368120947 is harder to memorize than 368 120 947).

The consequence for interface design is that we need to find groups of elements that the brain can process as one semantic unit to improve clarity and avoid overwhelming noise.

During question creation users mostly see forms with very little visual weighting. Obscure advanced options are presented just as visible as mandatory frequently used fields.

## Core issues

### No flow state possible

Sometimes the authors of tests have to enter dozens of questions

...

The goal is to allow a flow state, where the interface is an unobtrusive room for the users thoughts rather than causing them to think about the interface itself.

...

### Using the keyboard

Tabbing always starts with breadcrumbs

Adding multiple choice options not possible

...

### Too many features too visible

### Preview disconnected from creation

...

## Inspiration from other apps

### Flow state

Due to the limited screen space, many good mobile apps have mastered how to optimize interfaces by minimizing the amount of options shown at one time and leading users through multiple views relatively seamless.

If you learn a language in Duolingo or create a rental on Airbnb you are lead through many little steps through onboardings and bite sized prompts. The screens with the most options are usually setting or selection screens probing for the user intent. The actual work process is then done in very minimal interfaces step by step.

Even on larger desktop screens, there are use cases for minimal interfaces: Distraction free text editors are very popular among writers and programmers.

For presentations there are markdown based presentation tools like Reveal.js or Marp. Slidebean completely splits up content from design as a distinct two step process, so the user can be either in the writing or design mindset, but doesn't have to jump back and forth between them like in Power Point.

...

### Decoupling scoring from question creation

...

### WYSIWYG makes previews unnecessary

...

### Fast keyboard navigation

...

## Recommendations

### Creating questions as a flow

...

#### Minimizing page loads

...

### Hide and decouple advanced features

...

### Keyboard navigation: Flow feature or accessibility patch?

...
