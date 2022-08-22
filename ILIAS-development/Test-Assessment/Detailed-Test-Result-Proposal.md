# To Do & Open Questions

## Presentation Table

### Allowing other UI elements in content

Currently, anything in the content area of the presentation table must be a listing element. To make this view possible, the content area needs to accept other types like a UI panel or UI legacy element that can display the rendered questions. Which element exactly is best suited for this purpose needs to be discussed.

### Further Fields wastes space in this context

Since we only have 4-5 properties to populate the further fields area with, this section remains quite small.

If we chose a split layout, the further fields take horizontal space that squeeze the two questions uncomfortably narrow.

If we display the questions one after the other, there is a large empty space below them. In case of allowing no further fields, important fields should probably stay visible so that no displayed data is lost.

If we choose to display the best possible solution inside the questions (no split view), the further field layout could probably stay as is.

## New/extended UI Component?

Instead of just rendering hard-coded HTML, displaying the questions side by side could be done by an UI compnent. We could add a split panel to the UI component or a column layout UI component.

Otherwise the HTML layout could be written in a classic HTML template as it often is.
