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


### screen.py ends here
