"""Tweaked base application class."""

##############################################################################
# Python imports.
from typing import Generic

##############################################################################
# Textual imports.
from textual.app import App, ReturnType
from textual.binding import Binding
from textual.content import Content
from textual.markup import MarkupError
from textual.notifications import SeverityLevel


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
        OptionList{
            scrollbar-background: $panel;
            scrollbar-background-hover: $panel;
            scrollbar-background-active: $panel;
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

    def notify(
        self,
        message: str,
        *,
        title: str = "",
        severity: SeverityLevel = "information",
        timeout: float | None = None,
        markup: bool = True,
    ) -> None:
        """Create a notification.

        Args:
            message: The message for the notification.
            title: The title for the notification.
            severity: The severity of the notification.
            timeout: The timeout (in seconds) for the notification, or `None` for default.
            markup: Render the message as content markup?

        Notes:
            See the [Textual docs for `notify`][textual.app.App.notify] for full details.

            This is a markup-safe version of the `notify` method. Textual
            has changed how it handles markup and has now decided that
            broken markup should crash your application; imagine if browsers
            did that! So this is a sensible approach to handling unexpected
            markup-looking text.

            The `markup` parameter is still used; but if `markup` is
            [`True`][True] a test call to
            [`Content.from_markup`][textual.content.Content.from_markup] is
            performed and, if `MarkupError` is raised `markup` is forced to
            [`False`][False].

            Surprise markup [should not be the application user's
            concern](https://en.wikipedia.org/wiki/Principle_of_least_astonishment).
        """
        if markup:
            try:
                _ = Content.from_markup(message)
            except MarkupError:
                markup = False
        return super().notify(
            message, title=title, severity=severity, timeout=timeout, markup=markup
        )


### app.py ends here
