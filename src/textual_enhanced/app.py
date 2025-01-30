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
    """The Textual App class, with some tweaks."""

    CSS = """
    CommandPalette > Vertical {
        width: 75%; /* Full-width command palette looks kinda unfinished. Fix that. */
        background: $panel;
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
        /* The header icon serves no useful purpose. Remove it. */
        HeaderIcon {
            visibility: hidden;
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
