# textual-enhanced

## Introduction

This library is a mildly-opinionated set of enhancements and extras for the
[Textual framework](https://textual.textualize.io/), mainly aimed at how I
like my own Textual apps to look and work. I've written this as a common set
of tweaks I want for my own Textual apps. It might be useful for yours too.

## Style choices

I tend to like the same style choices for all of my applications, this
library implements the following:

- All vertical scrollbars are set to one character in width, by default (in
  my applications I try really hard to avoid horizontal scrolling, so it's
  nice to make scrollbars less obtrusive given I almost always only have
  vertical bars).
- The icon on the left of the [`Header`][textual.widgets.Header] widget is
  hidden.
- The ability to click to expand the [`Header`][textual.widgets.Header] is
  disabled.
- the command palette is modified so that it doesn't take up the full width
  of the screen (the full-width version makes it near-unreadable in wide
  terminals and overall makes the command palette look like it's been
  forgotten about).
- <kbd>super</kbd>+<kbd>x</kbd> is added as an alternative method of calling
  the command palette (yes, I am an Emacs user, can you tell?).
- <kbd>:</kbd> is added as an alternative method of calling the command
  palette (because I am nice to vi(m) users).
- The command palette's search icon is removed.
- The command palette's `background` is set to `$panel` by default.

[//]: # (index.md ends here)
