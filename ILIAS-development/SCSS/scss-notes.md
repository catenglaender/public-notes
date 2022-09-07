# How could loading and using look

in delos

```SCSS
@use 'variables/colors';
```

in variables/_colors.scss

```SCSS
$brand-primary: blue;
```

Underscore _file.scss means it's a partial, never compiled on its own.

## Index file is loaded when loading folder

- variables
    - _index.scss
    - _brand-colors.scss
    - _alert-colors.scss

in delos.scss:

```SCSS
@use 'variables';
```

in variables/_index.scss

```SCSS
@use 'brand-colors';
@use 'alert-colors'
```

