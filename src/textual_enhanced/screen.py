"""A Textual screen, with tweaks."""

##############################################################################
# Python imports.
from typing import Generic

##############################################################################
# Textual imports.
from textual.command import CommandPalette
from textual.screen import Screen, ScreenResultType

##############################################################################
# Local imports.
from .commands import CommandsProvider
from .dialogs import HelpScreen


##############################################################################
class EnhancedScreen(Generic[ScreenResultType], Screen[ScreenResultType]):
    """A Textual screen with some extras."""

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
