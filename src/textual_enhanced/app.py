"""Tweaked base application class."""

##############################################################################
# Python imports.
from typing import Generic

##############################################################################
# Textual imports.
from textual.app import App, ReturnType
from textual.binding import Binding


##############################################################################
class EnhancedApp(Generic[ReturnType], App[ReturnType]):
    """The Textual [App class][textual.app.App]  with some styling tweaks.

    `EnhancedApp` adds no code changes, but it does implement a number of
    global styles that make a Textual app look just how I like. It also adds
    some extra default bindings for calling the command palette.
    """

    CSS = """
    CommandPalette > Vertical {
        width: 75%; /* Full-width command palette looks kinda unfinished. Fix that. */
        background: $panel;
        #--input {
            border-top: hkey $border;
        }
        OptionList{
            scrollbar-background: $panel;
            scrollbar-background-hover: $panel;
            scrollbar-background-active: $panel;
            border-bottom: hkey $border;
        }
        SearchIcon {
            display: none;
        }
    }

    /* Make the LoadingIndicator look less like it was just slapped on. */
    LoadingIndicator {
        background: transparent;
    }

    /* Remove cruft from the Header. */
    Header {
        /* I have zero use for the header icon or the clock. */
        HeaderIcon, HeaderClockSpace {
            display: none;
        }

        /* Ditto the tall version of the header. Nuke that. */
        &.-tall {
            height: 1 !important;
        }
    }

    /* General style tweaks that affect all widgets. */
    * {
        /* Let's make scrollbars a wee bit thinner. */
        scrollbar-size-vertical: 1;
    }
    """

    BINDINGS = [
        Binding(
            "ctrl+p, super+x, :",
            "command_palette",
            "Commands",
            show=False,
            tooltip="Show the command palette",
        ),
    ]


### app.py ends here
