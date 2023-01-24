## 1 Initial Problem
The current detailed result view of the Test Assessment
* requires many clicks and much scrolling to navigate,
* renders questions with no regard to the content styles,
* and is optimized for printing, but many users evaluate test results on screens.

This impacts the user experience negatively:
* Users see the questions in an unfamiliar, unstyled look causing them to wonder why the view "looks broken".
* The lack of filters and sorting can makes evaluating tests with many questions difficult and time consuming.

For developers there are drawbacks to how this view is currently assembled:

* The view is rendered with deprecated legacy methods instead of using kitchen sink elements from the UI framework.
* Some bugs and visual glitches are tricky to fix, because the content styles and the print style rendering clash in unexpected ways.

## 2 Conceptual Summary

We propose a new detailed result view that is
* using the global content style appearance for questions to minimize confusion and visual glitches
* enabling the user to intuitively navigate to the information they seek using a flexible and filterable presentation table,
* making maintenance easier by using modern UI components from the UI framework.

### Layered Information Architecture

The current implementation has an overview table at the top and a long list of question content below. A presentation table will present these two layers of information in the same spot:

* Layer 1: The collapsed rows of the presentation table will provide an uncluttered overview by showing only the most relevant information for the average user (e.g. which questions were answered (in)correctly)
* Layer 2: On click, a row expands in place and reveals the content area with the question text, the answers and more information for in-depth test evaluation use cases.

Filters and View Controls will help the user to narrow down which questions are shown and how they are sorted.

### Current implementation

![](./img/detailed-results_old-overview.jpg)

### Draft for the new result view

![](./img/detailed-results_expaned-item-multiple-choice.jpg)

## 3 User Interface Modifications

### 3.1 List of Affected Views
* ilrepositorygui > ilTestEvaluationGUI > outParticipantsPassDetails
* UI component Presentation Table

### 3.2 User Interface Details

#### Layer 1: Maximizing overview

This is how the table of contents at the top of the detailed result page currently looks

![](./img/detailed-results_old-table-of-content.jpg)

The rendering as a legacy table has some disadvantages:
* Some properties are not of immediate interest to the average user, yet they take equal or more space than highly relevant information (e.g. Requested Hints vs Percentage Solved)
* The property most valuable for understanding how well a question was answered is the Percentage Solved column, but because it's far away from the Question Title the eyes need to constantly dart back and forth.

Here is an example of how the new view could look with all questions wrapped within a collapsed presentation table:

![](./img/detailed-results_all-collapsed.jpg)

The collapsed rows with very condensed information helps users to
* skim through the list of answers without being distracted by too many properties
* get a rough feeling for the weakest and strongest parts of the test results without even opening a single question
* quickly identify and jump to specific questions that they know about (e.g. a participant could find that one Cloze Test question they had trouble with during the test by focusing on the question title and type)

To support quick identification
* correct and incorrect/incomplete answers are more clearly distinguishable by an icon directly in front of the title
* the values for reached and maximum points are pulled closer together instead of being pulled apart by a lot of white space in the legacy table
* the tables view controls allow to quickly filter e.g. for complete and incorrect/incomplete answers

#### Layer 2: Drilling down for details

If the user is interested in the specifics of one or multiple answers, they can simply click on the row of the presentation table to expand the content area and reveal the second layer of information, without loosing the position in the table.

In the current implementation the viewport jumps to a question block inside a long list, which is rendered in this way:

![](./img/detailed-results_old-multiple-answers-rendering.jpg)

This stripped down rendering of questions makes focused work difficult:
* The feedback blends in with the body of the question
* The other question blocks clutter and overwhelm the view even though they might not be of interest

Here is an example for a more familiar and segmented rendering inside the presentation table:

![](./img/detailed-results_expaned-item.jpg)

Although the user might have many different reasons for looking at this second layer of information, the presentation table still helps us to improve the user experience:

* users don't loose their position in the table when opening or closing a row entry
* familiar styling makes important areas like the feedback box stand out and helps distinguish e.g. the question text from the rest of the answer.
* more properties can be revealed for more rare use cases without taking up an entire table column (e.g. the question ID)

### Filters for quicker evaluation







{ For each of these views please list all user interface elements that should be modified, added or removed. Please provide the textual appearance of the UI elements and their interactive behaviour. }

### 3.3 New User Interface Concepts

#### Colum Panel

#### New Presentation Table Features

#### New Column Panel

#### New View Controls

{ If the proposal introduces any completely new user interface elements, you might consult UI Kitchen Sink in order to find the necessary information to propose new UI-Concepts. Note that any maintainer might gladly assist you with this. }

### 3.4 Accessibility Implications
{ If the proposal contains potential accessibility issues that are neither covered by existing UI components nor clarified by guidelines, please list them here. For every potential issue please either propose a solution or write down a short risk assessment about potential fallout if there would be no solution for the issue. }

## 4 Technical Information
{ The maintainer has to provide necessary technical information, e.g. dependencies on other ILIAS components, necessary modifications in general services/architecture, potential security or performance issues. }

## 5 Privacy
{ Please list all personal data that will need to be stored or processed to implement this feature. For each date give a short explanation why it is necessary to use that date. }

## 6 Security
{ Does the feature include any special security relevant changes, e.g. the introducion of new endpoints or other new possible attack vectors. If yes, please explain these implications and include a commitment to deliver a written security concept as part of the feature development. This concept will need an additional approvement by the JourFixe. }

## 7 Contact
Author of the Request: Engländer, Ferdinand
Maintainer:
Implementation of the feature is done by: {The maintainer must add the name of the implementing developer.}

## 8 Funding
If you are interest in funding this feature, please add your name and institution to this list.

## 9 Discussion