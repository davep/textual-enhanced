"""A Textual screen, with tweaks."""

##############################################################################
# Python imports.
from contextlib import contextmanager
from typing import Generic, Iterator

##############################################################################
# Textual imports.
from textual.command import CommandPalette
from textual.css.query import QueryType
from textual.screen import Screen, ScreenResultType

##############################################################################
# Local imports.
from .commands import CommandsProvider
from .dialogs import HelpScreen


##############################################################################
class EnhancedScreen(Generic[ScreenResultType], Screen[ScreenResultType]):
    """A Textual screen with some extras."""

    @contextmanager
    def busy_looking(self, selector: str | type[QueryType]) -> Iterator[None]:
        """Provides a context that makes a widget look busy.

        A simple helper that turns this:

        ```python
        self.query_one(Display).loading = True
        self.do_something_that_takes_a_moment()
        self.query_one(Display).loading = False
        ```

        into this:

        ```python
        with self.busy_looking(Display):
            self.do_something_that_takes_a_moment()
        ```
        """
        (busy_widget := self.query_one(selector)).loading = True
        try:
            yield
        finally:
            busy_widget.loading = False

    def show_palette(self, provider: type[CommandsProvider]) -> None:
        """Show a particular command palette.

        Args:
            provider: The commands provider for the palette.
        """
        self.app.push_screen(
            CommandPalette(
                providers=(provider,),
                placeholder=provider.prompt(),
            )
        )

    def action_help_command(self) -> None:
        """Show the help screen.

        Rather than use Textual's own help facility, this shows [my own help
        screen][textual_enhanced.dialogs.HelpScreen].
        """
        self.app.push_screen(HelpScreen(self))

    def action_change_theme_command(self) -> None:
        """Show the Textual theme picker command palette."""
        self.app.search_themes()


### screen.py ends here
