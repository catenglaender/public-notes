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

In the table below we counted clicks and view changes when

* starting on the overview screen of an empty test or quiz
* creating one single choice true/false question,
* creating one multiple choice question with four options,
* assigning 10 points to the correct answers,
* ending on the overview screen

Screen recordings of the question creation in ILIAS and on Quiz-Maker.com:

![](./img/Click-Count_Test_ILIAS_Timelapse.gif)

![](./img/Click-Count_Test_quiz-maker_Timelapse.gif)

| Tool            | Click Count | Change of View | Set 10 points for correct answers |
| --------------- | ----------- | -------------- | --------------------------------- |
| ILIAS           | 33          | 8              | possible                          |
| Typeform        | 19          | 3              | possible                          |
| Quiz-Maker.com  | 18          | 3              | possible                          |
| H5P             | 16          | 0              | not possible                      |
| Articulate Rise | 13 - 16     | 0              | not possible                      |

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

### No flow during question creation

Sometimes the authors of tests have to enter dozens of questions. However, in its current state the interface requires many clicks and view changes that slow the user down or interrupt their focus.

For example, to finish one question and create another the user has to...
* finish question with a click on "save and return" in form actions
  
![](img/2023-09-25-13-55-13.png)

* exit the preview by clicking on "Back to the Test" in sub tabs

![](img/2023-09-25-13-56-57.png)

* click on "Create Question" in Questions overview page

![](img/2023-09-25-13-58-53.png)

That's three clicks in three different locations across three views. That's too many for a user intent that we can be relatively certain of: most of the time when a user creates one question, they also want to create another one.

Compare this to Quiz-Maker.com where creating a new question is always possible at the bottom of the view and you never need to indicate that you are done editing a question:

![](img/2023-09-25-14-01-38.png)

Additionally, there is no interrupting validation of the user input in Quiz-Maker on this screen.

In ILIAS you may forget to add "0" as a point value for the incorrect answers. The resulting error causes the page to reload and scroll up which is quite jarring to a user needing to enter many questions.

![](img/2023-09-25-14-10-14.png)

The goal should be to allow a flow state, where the interface is an unobtrusive room for the user's thoughts rather than causing them to think about the interface itself.

### Using the keyboard

While keyboard navigation in ILIAS is technically possible, it is far from being a pleasant experience. After every page reload the keyboard focus tabbing begins at the breadcrumb bar, which is not at all relevant to a user wanting to blaze through the input of many questions.

We believe that a fluent and consistent keyboard support can make the input of many questions a lot easier as moving the hand from keyboard to mouse repeatedly can be perceived as friction for the user experience.

In Quiz Maker, keyboard focus is automatically set to the question text after creating a new question, which feels very natural and saves a click.

### Too many features too visible

Because ILIAS supports many different use cases there are many features that might not be interesting to all authors. ILIAS often shows these features with the same visual priority or even forces an input.

In our research, we noticed that some tools (Quiz-Maker, Typeform) keep scoring hidden from the average user and just award answers marked as correct with 1 point unless otherwise specified in an optional second step.

The Lifecycle field is the most useful as a bulk operation in an overview screen. Setting all questions to "Final" during creation is a huge waste of time.

While skipping this step is probably not suitable for an exam, not being forced to enter point values greatly speeds up some use cases e.g. the creation of little test that someone might want to add to chapters in a learning sequence.

### Preview disconnected from creation



...

## Inspiration from other apps

### Flow state

Due to the limited screen space, many good mobile apps have mastered how to optimize interfaces by minimizing the amount of options shown at one time and leading users through multiple views with ease.

If you learn a language in Duolingo or create a rental on Airbnb you are guided in many little steps through onboardings and bite sized prompts. The screens with the most options are usually setting or selection screens probing for the user intent. The actual work process is then done in very minimal interfaces step by step.

Even on larger desktop screens, there are use cases for minimal interfaces: Distraction free text editors are very popular among writers and programmers. Project management software like Asana, Trello and Active Collab are able to display quite complex entities with many properties, but reduce the amount of information displayed in certain views.

Markdown based presentation tools like Reveal.js or Marp and the pitch deck service Slidebean separate content creation from design as a distinct two step process. This way the user can be either in the writing or design mindset (and their distinct mental models) and doesn't have to jump back and forth between both like in Power Point.

We believe that there are two things from these examples we should re-create in ILIAS:
* reducing and segmenting the interface where it feels natural and smooth to the user (and vice versa combine steps that the user would expect to be combined)
* take inspiration from data entry, writing and markdown-based tools that allow a flow state for entering large amounts of texts without ever interrupting the user with unnecessary obstacles.

### Decoupling scoring from question creation

...

### WYSIWYG makes preview steps unnecessary

...

### Fast keyboard navigation

...

## Incremental Improvements

### Minimizing page loads

...

### Validation and error messages

...

### Overview during question creation

...

### Hide and decouple advanced features

### Duplicate Questions

### Reasonable Defaults

Single Choice questions should have true and false as a default.

Cloze Questions could have an example input placeholder text with one gap in it to demonstrate how it's done.

...

### Keyboard navigation: Feature not accessibility patch!

Focus on question title

...

## Overall Model

### Markdown

### Full WYSIWYG

### Oveview in Slate & new form features