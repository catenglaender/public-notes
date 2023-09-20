# Tips

## Make variable definitions to default variables

Search and replace in VSCode, regular expression switched on

find:
```regex
(\$.*):(.*);
```
replace:
```regex
$1:$2 !default;
```

turns
```SCSS
$il-mainbar-btn-padding: 0
$il-mainbar-btn-label-icon-gap: $il-padding-xs-vertical;
```

into
```SCSS
$il-mainbar-btn-padding: 0 !default;
$il-mainbar-btn-label-icon-gap: $il-padding-xs-vertical !default;
```