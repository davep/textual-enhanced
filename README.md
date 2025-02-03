# textual-enhanced

## Introduction

This library is a mildly-opinionated set of enhancements and extras for the
Textual framework, mainly aimed at how I like my own Textual apps to look
and work. I've written this as a common set of tweaks I want for my own
Textual apps. It might be useful for yours too.

## Tweaks to Textual

### App-wide

- All vertical scrollbars are set to one character in width, by default (in
  my applications I try really hard to avoid horizontal scrolling, so it's
  nice to make scrollbars less obtrusive given I almost always only have
  vertical bars).

### The `Header` widget

- The icon on the left is hidden.
- The ability to click to expand the header is disabled.

### The command palette

I've tweaked the command palette so that:

- It doesn't take up the full width of the screen.
- <kbd>super</kbd>+<kbd>x</kbd> is added as an alternative method of calling
  it.
- <kbd>:</kbd> is added as an alternative method of calling it.
- The search icon is removed by default.
- The `background` is set to `$panel` by default.

### The loading indicator

The background is set to `transparent` by default.

## Additional Features

### With-some-batteries command palette/bindings

TODO: Explain.

## Widgets

### `EnhancedOptionList`

Adds `.preserved_highlight`, which can be used like:

```python
with stuff.preserved_highlight:
   ...rebuild the content of the list...
```

Adds a few more navigation keys.

Works around https://github.com/Textualize/textual/issues/5489.

Mild style tweaks.

### `TextViewer`

## Dialogs

### `HelpScreen`

TODO: Explain.

### `QuickInput`

TODO: Explain.

## Tools

### `add_key`

TODO: Explain.

[//]: # (README.md ends here)
