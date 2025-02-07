"""Command classes and a provider for common commands."""

##############################################################################
# Local imports.
from .command import Command
from .provider import CommandHits, CommandsProvider


##############################################################################
class Help(Command):
    """Show help for and information about the application"""

    BINDING_KEY = "f1, ?"
    SHOW_IN_FOOTER = True


##############################################################################
class ChangeTheme(Command):
    """Change the application's theme"""

    BINDING_KEY = "f9"


##############################################################################
class Quit(Command):
    """Quit the application"""

    BINDING_KEY = "f10, ctrl+q"
    SHOW_IN_FOOTER = True


##############################################################################
class CommonCommands(CommandsProvider):
    """Provides some common top-level commands for the application."""

    def commands(self) -> CommandHits:
        """Provide the main application commands for the command palette.

        Yields:
            The commands for the command palette.
        """
        yield Help()
        yield ChangeTheme()
        yield Quit()


### common.py ends here
