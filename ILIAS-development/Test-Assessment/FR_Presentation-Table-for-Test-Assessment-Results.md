## 1 Initial Problem
The current detailed result view of the Test Assessment
* requires many clicks and much scrolling to navigate,
* renders questions with no regard to the content styles,
* and is optimized for printing, but many users evaluate test results on screens.

This poses challenges for both users and developers:
* Users see the questions in an unfamiliar, unstyled look - which causes them to wonder why the view "looks broken".
* The lack of filters and view controls make it hard to narrow down and structure test results with many questions.
* The view is rendered with deprecated legacy methods instead of using kitchen sink elements from the UI framework.
* Some bugs and visual glitches are tricky to fix, because the content styles and the stripped down print rendering of the questions clash in unexpected ways.

## 2 Conceptual Summary

We propose a detailed result view that is
* using the global content style appearance for questions to minimize confusion and visual glitches
* enabling the user to drill down to the information they seek using a flexible and filterable presentation table,
* making maintenance easier by using modern UI components from the UI framework

### Maximizing overview

Here is an early mockup of how the view could look with all questions collapsed:

### Drilling down for details

### Filters for quicker evaluation

## 3 User Interface Modifications

### 3.1 List of Affected Views
* ilrepositorygui > ilTestEvaluationGUI > outParticipantsPassDetails
* the UI component Presentation Table requires

### 3.2 User Interface Details
{ For each of these views please list all user interface elements that should be modified, added or removed. Please provide the textual appearance of the UI elements and their interactive behaviour. }

### 3.3 New User Interface Concepts
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