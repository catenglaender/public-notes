# Element Types in toolbar

* Action: Download Export (e.g. "Download [Event] Files")
* Action: Manage connected status/attribute
* Action: Mark (as completed in LSO kiosk mode)
* Action: Submit/Suspend Input Mode (like survey, test)
* Action: change a system setting (activate translation for Page Editing)
* Action: create sub-item ("Add magazine object", "Create appointment", add forum, some exports)
* Action: edit this item/view (open in page editor, email)
* Action: join with a specific role
* Action: print (Notes, LSO kiosk mode, learning module)
* Action: query specific item by freely entered text (Change to user by entering a name)
* Action: search query
* Bulk-Action: Change to template selected from dropdown (applied didactic template in Category Permissions)
* Bulk-Action: Import (Users in Local User Administration)
* Bulk-Action: Message many (Mail to group members)
* Bulk-Action: process multiple sub-items (copy, move, delete, mark)
* Bulk-Action: save a change of multiple sub-items (save sort order)
* Interface: Show/hide sidebar
* Launch: Start a mode
* Navigation: Go to other page (similar to navigating to subtab e.g. learning module)
* Navigation: Next/Previous view/item in line (LSO kiosk mode, Survey Questions)
* View Controls for sub-items in view (sortation in Notes or range of items in calendar, forum sortation)

# Observations and Questions

* What options go into navbar, sub-tabs, table command row or header action dropdown and why?
* View controls tend to be in the toolbar, but filters (with the exception of search query inputs) are often separate
* Visual spacing and bars sometimes separate buttons that feel like they are part of the same semantic groups
* Buttons are relevant to varying degrees, but they often are just default btns. Sometimes there is a btn primary.

# Rivals

* Action Dropdown in Header
* Filters
* `ilTableCommandRow`

# Multiple constructs that look similar

* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`
* B: `<div class="ilAdminRow">[...]<nav class="ilToolbar navbar navbar-default " id="2">`
* part of table but sometimes it's rendered directly under the sub-tabs, so it looks like it's the repository toolbar, C: `<div class="ilTableOuter"><div class="ilTableCommandRowTop form-inline">`
* D: `<div class="container-fluid" id="ilContentContainer">[...]<div class="ilToolbar" id="il_search_toolbar">`
* E: `<nav class="ilToolbar navbar-default ilLSOKioskModeNavigation" role="navigation" id="2">` (LSO Kiosk Mode)
* F: `<form id="il-svy-output-form" [...]><table class="fullwidth">`
* G: `<nav class="ilToolbar navbar navbar-default " id="2"><div class="container-fluid">` (during Test)
* H: `<div class="ilTstNavigation">` (during Test)
* I: `<nav class="ilToolbar navbar navbar-default " id="tst_results_toolbar"><div class="container-fluid">` (Test Result Overview)

# Occurences

## Calendar

![](img/2023-04-04-16-45-26.png)

* Viewcontrols Day/Week/Month, pagination day/week/month
* Action: create sub-item ("Create Appointment")
* Action "Download [Event] Files"
*  https://test8.ilias.de/ilias.php?baseClass=ildashboardgui&cmdNode=9e:61:60&cmdClass=ilCalendarMonthGUI
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Repository Category Object

![](img/2023-04-04-16-55-23.png)

* Action: create sub-item ("Add New Item")
* Action: edit this item ("Customize Page")
* "Action" dropdown doesn't have either options - what options go into navbar, sub-tabs or header action dropdown?
* https://test8.ilias.de/ilias.php?baseClass=ilrepositorygui&ref_id=7700
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Repository Manage View

![](img/2023-04-04-16-57-51.png)

* Action: process one or multiple sub-items
* has the arrow of a `ilTableCommandRow`
* B: `<div class="ilAdminRow">[...]<nav class="ilToolbar navbar navbar-default " id="2">`

## Repository Sorting View

![](img/2023-04-04-17-05-31.png)

* Action: save a change of sub-items (sort order of sub-items)
* B: `<div class="ilAdminRow">[...]<nav class="ilToolbar navbar navbar-default " id="2">`

## Repository Category > Settings > Multilingualism

![](img/2023-04-04-17-08-33.png)

* Action: create sub-item
* Action: change a system setting (activate translation for Page Editing)
* `ilTableCommandRow` underneath fakes the look of a toolbar
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Repository Category > Settings > Filter

![](img/2023-04-04-17-16-13.png)

* Action: jump to deeper settings (fieldselection for filter)
* What are you supposed to actually do on this screen? couldn't it just show the fieldselection instead?
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Repository Category > Local User Administration

![](img/2023-04-04-17-24-03.png)

* Action: add sub-item (Local User)
* Bulk-Action: Import (Users in Local User Administration)
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Repository Category > Export

![](img/2023-04-04-17-52-43.png)

* Action: add sub-item
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Repository Category > Permissions

![](img/2023-04-04-17-54-47.png)

* Bulk-Action: Change to template selected from dropdown
* Action: add sub-item (Add New Local Role, Import Role)
* Potential rival on same screen: filter and save button

## Repository Category > Permission of User

![](img/2023-04-04-17-57-59.png)

* Action: query specific items by freely entered text
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Search

![](img/2023-04-05-11-10-17.png)

* Action: search query items by freely entered text
* D: `<div class="container-fluid" id="ilContentContainer">[...]<div class="ilToolbar" id="il_search_toolbar">`

## Learning Sequence

![](img/2023-04-05-11-21-10.png)

* Navigation: Next/Previous
* Action: Mark (as completed)
* Action: print
* Direct Rivals:
  * Dropdown with "Edit Page, Info, Notes"
  * Close View
* E: `<nav class="ilToolbar navbar-default ilLSOKioskModeNavigation" role="navigation" id="2">`

## Private Notes

![](img/2023-04-05-11-47-17.png)

* Action: Download Export
* View Controls for sub-items in view
* Why are print and HTML Export visually separated?
* Direct Rivals:
  * Filter
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## File Info

![](img/2023-04-05-12-00-05.png)

* Action: Download Export
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Group > Members

![](img/2023-04-05-12-03-02.png)

* Bulk-Action: Message many (Mail to members)
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Learning Module

![](img/2023-04-11-10-50-58.png)

* Navigation: Go to other page (info page)
* Action: Manage connected status/attribute
* Action: print
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Mediapool

![](img/2023-04-11-11-01-48.png)

* Action: create sub-item
* in TableControls:
  * Bulk-Action: process multiple sub-items (copy, move, delete)
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`
* C: `<div class="ilTableOuter"><div class="ilTableCommandRowTop form-inline">`

## E-Mail

![](img/2023-04-11-11-06-18.png)

* Action: edit this item/view (Forward, Print, Delete, Move)
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Survey - Landing

![](img/2023-04-11-11-14-28.png)

* Action: join with a specific role
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Survey - Questions

![](img/2023-04-11-11-19-44.png)

* Navigation: Next/Previous
* Navigation: Go to other page
* Action: Submit/Suspend Input Mode
* F: `<form id="il-svy-output-form" [...]><table class="fullwidth">`

## Forum

![](img/2023-04-11-11-32-00.png)

* Action: create sub-item
* Bulk-Action: process multiple sub-items
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Forum Thread

![](img/2023-04-11-11-34-59.png)

* Action: create sub-item
* Bulk-Action: process multiple sub-items
* View Controls for sub-items in view
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Blog

![](img/2023-04-11-11-40-11.png)

* Navigation: Next/Previous Pagination/Month/Post
* Action: edit this item/view
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Test - Info Tab

![](img/2023-04-18-11-25-59.png)

* Launch: Start a mode (start test)
* A: `<div class="container-fluid ilToolbarContainer">[...]<nav class="ilToolbar navbar navbar-default " id="1">`

## Test - Running Test

![](img/2023-04-18-11-40-29.png)

* 3 Toolbar designs in one view
* Interface: Show/hide sidebar
* Navigation: Go to other page
* Action: Submit/Suspend Input Mode
* Interaction directly with specific question is part of a shy dropdown
* G: `<nav class="ilToolbar navbar navbar-default " id="2"><div class="container-fluid">`
* H: `<div class="ilTstNavigation">`

## Test Result

![](img/2023-04-18-11-42-08.png)

* Action: print
* Action: Download Export
* I: `<nav class="ilToolbar navbar navbar-default " id="tst_results_toolbar"><div class="container-fluid">`