In this paper, we investigate how optional or advanced sections in complex ILIAS forms could be presented.

We will especially look at common best practices for segmenting a form and hiding the parts that are less relevant for the current user.

The goal is to improve the user experience by
* reducing visual noise that can be overwhelming
* speeding up the process of filling out complex forms

# Complex forms in ILIAS

Most objects in ILIAS are created by filling out a form. Often times the forms simply map a huge number of properties and settings onto one page.

Segmentation is achieved by sorting input fields into groups with a headline and by using the ILIAS sub-tabs. When the ILIAS sub-tabs are used to spread settings onto multiple pages, each page requires a click on the Save button before switching the tab.

Often times, many properties are mandatory for the creation of the object. This requirement is softened by many defaults that are pre-set.

# Issues with complex ILIAS forms

## Loosing overview

Especially forms meant for administrators and users with more permissive roles (we will call them "managing users" in this paper) tend to have so many input fields, checkboxes and dropdowns that it takes quite some time to look at every single option.

If you are a new user, you have to scan the entire form for options you might need because the grouping does not always help with the decision to ignore an entire section of the form. When options are spread over multiple sub-tabs, it's not always immediately clear which tabs can be ignored most of the time and which tabs might contain further relevant choices as they are presented with equal visual weight.

Even experienced users often have to invest a couple of seconds to search for that one specific option that they know exists somewhere.

## Can one type of form cover everything?

ILIAS forms look (with rare exceptions) the same in all contexts. A registration form on the frontend for end-users utilizes the same design and UI components as a complex setting screen for administrators.

However, those two use cases have vastly different requirements:
* For frontend forms, ease of use and a high conversion rate to collect information are the most important Key Performance Indicators.
* An administrativ form is a tool not only for creation, but also for frequently managing settings and often can be thought of as a control panel.

# Goal: Ease of use

Optional sections in ILIAS forms should meet the following goals:
* They should make forms more lean and less intimidating, especially for new users.
* Advanced or optional settings hidden away should still be easy to find and easy to access.
* We are looking for solutions that work for both end-user information input as well as for managing settings.

# User Intents

While using forms the users focus and main intention can be vastly different. These different focuses are mainly defined by...
* the user intent: What conscious goal does the user have?
* the mental model: What expectations based on previous experiences and learned patterns does the user have on how to achieve that goal?

For this analysis we had a look at many forms in ILIAS and sorted them into three general categories:

## Condensed information prompt

Sometimes forms are designed to collect a specific, small set of information (like a user registration, login, survey, quiz or contact form). In this case it's often expected that the user fills out or changes (almost) all fields and they often do so one field after the other in sequence.

While the submitted information can create an object in the software, the focus of such forms is often a frictionless conversion from query to submission.

Seeing a lot of fields that aren't applicable or relevant to the user can be confusing and deters some people from submitting the form. Consequently, these forms are often reduced to a selected, small amount of fields.

An object created by submitting an information prompt likely has many more properties under the hood that are being added automatically or by a managing user beforehand that the end-user will never see (pre-set user role, conditional logic, quiz evaluation, admin email address to receive a notification etc.).

### Examples:

Wikipedia User Registration

![](img/wikipedia_login.png)

A rating question in Typeform

![](img/typeform_star-rating.png)

## Object creation focus

In ILIAS many forms are an almost complete representation of an object's settings and properties. Most things that could possibly be defined about the object has a field.

During the initial creation of such an object (e.g. test, test question, course etc.) a managing user will probably fill out most fields and check if the pre-set default values are in line with their intentions.

While more experienced users will be better at jumping to the input elements that are required or relevant, it's still a sequential process most of the time. Named categories help to gain an overview.

## Checking and changing selectively

When a user wants to change an already existing object they are often thrown into the same form that was used for creating it.

However, when coming back to existing objects, the user intent is often different:
* Checking settings
* Changing settings

As the mental modal is no longer a sequential field by field processing, getting an overview and jumping to the relevant spot in the form is now the main focus.

So far ILIAS barely accommodates this mental model. Forms for editing objects and forms for editing objects are very often exactly the same

# Strategies & Best Practices

Fortunately, other projects had to solve similar challenges before us and we can get inspiration from their solutions.

## Reducing the amount of fields

It might seem obvious, but the best way to maintain a feeling of overview is to not have that many options in a form to begin with.

If there are fields that are barely used or are left overs from abandoned or never finished concepts, they should either be brought to full functionality or removed. Moving such fields to an hidden advanced or optional section only moves the problem out of direct sight, but does not solve it.

When following the approach that all properties and settings of an object are mapped almost completely to a form, administrators and managing users will be left with quite a few options. However, there might still be possibilities to remove fields:

The business software ERPNext for example allows administrators to remove not mandatory field from forms permanently for the entire instance. This makes a lot of sense if an instance is not ever using certain functionalities as it reduces unnecessary weight of the interface for all users.

Some CRM software like WordPress distinguishes between end-user facing content and setting forms for the managing users. The advantage is that most WordPress form plugins only expose forms that are greatly simplified and optimized for conversion to the average user and only administrators see the complex setting forms where everything is visible.

## Revealing more options

How do most forms on the web and in SaaS handle the actual hiding and showing of additional form elements?

During this chapter we will reference the book Web Form Design: Filling in the Blanks by Luke Wroblewski when referring to studies and user evaluations comparing different methods and their perceived ease of use and satisfaction ratings.

### Conditional visibility

We already have a UI component in ILIAS that allows hiding and showing sub-forms when a checkbox or radio box is ticked (named Optional Group and Switchable Group).

This is an example of conditional visibility that can be set up in many form builders and is frequently used in forms all over the internet.

User testing rated revealing sub-forms by checking radio buttons as follows:
* has the advantage of always keeping all the initial options — and a person’s
selection among those options — visible

Conditional visibility could potentially also be triggered by other field types e.g. a dropdown:

![](img/codepen_conditional-dropdown.gif)



### Accordion

One of the most frequently suggested tools to group and hide content

Screenshot from a StackExchange conversation about validating long forms:

![](img/stackexchange_accordion.png)

## Tabs and form steps

WordPress Plugin Multi-Step Checkout for WooCommerce by Silyk Press

![](img/wp-multi-step-checkout_payment.png)

### Editing and viewing mode

### Branching conversational forms (and wizards)





## Conversational forms and wizards





# Possible solutions for ILIAS

## Distinguish between front-end and admin forms

## Revealing further inputs in ILIAS 9

ILIAS 9 has UI components called Optional Group and Switchable Group that can reveal further input fields when a checkbox or radio button is ticked. This UI component is not widely used yet and there are many legacy modules where this feature could only be utilized after a switch to the new UI framework.

These components could be a very important tool when dealing with advanced and branching form options.

## Wizards for filling out in sequence

## Optimized for viewing and checking

## Multi-column approaches