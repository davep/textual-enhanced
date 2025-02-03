"""Provides a simple help screen."""

##############################################################################
# Python imports.
from inspect import cleandoc
from operator import methodcaller
from typing import Any
from webbrowser import open as open_url

##############################################################################
# Textual imports.
from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Center, Vertical, VerticalScroll
from textual.dom import DOMNode
from textual.screen import ModalScreen, Screen
from textual.widgets import Button, Markdown

##############################################################################
# Textual enhanced imports.
from ..commands import Command
from ..tools import add_key


##############################################################################
class HelpScreen(ModalScreen[None]):
    """The help screen."""

    CSS = """
    HelpScreen {
        align: center middle;

        &> Vertical {
            width: 75%;
            height: 90%;
            background: $panel;
            border: solid $border;
        }

        Markdown, MarkdownTable {
            padding: 0 1 0 1;
            background: transparent;
        }

        MarkdownH1 {
            padding: 1 0 1 0;
            background: $foreground 10%;
        }

        VerticalScroll {
            scrollbar-gutter: stable;
            scrollbar-background: $panel;
            scrollbar-background-hover: $panel;
            scrollbar-background-active: $panel;
        }

        Center {
            height: auto;
            width: 100%;
            border-top: solid $border;
        }
    }
    """

    BINDINGS = [("escape, f1", "close")]

    def __init__(self, help_for: Screen[Any] | None = None) -> None:
        """Initialise the help screen.

        Args:
            help_for: The screen to show the help for.
        """
        super().__init__()
        if help_for is None:
            help_for = self.app.screen
        self._context_help = ""
        for node in (
            help_for.focused if help_for.focused is not None else help_for
        ).ancestors_with_self:
            if node.HELP is not None:
                self._context_help += f"\n\n{cleandoc(node.HELP)}"
            self._context_help += self.command_help(node)

    def _all_keys(self, command: Command) -> str:
        """Render all the keys for the given command.

        Args:
            command: The command to get all the keys for.

        Returns:
            A string listing all the keys for the command.
        """
        return ", ".join(
            self.app.get_key_display(Binding(key.strip(), ""))
            for key in command.binding().key.split(",")
        )

    def command_help(self, node: DOMNode) -> str:
        """Build help from the commands provided by a DOM node.

        Args:
            node: The node that might provide commands

        Returns:
            The help text.
        """
        if (commands := getattr(node, "COMMAND_MESSAGES", None)) is None:
            return ""
        keys = "| Command | Key | Description |\n| - | - | - |\n"
        for command in sorted(commands, key=methodcaller("command")):
            keys += f"| {command.command()} | {self._all_keys(command)} | {command.tooltip()} |\n"
        return f"\n\n{keys}"

    @property
    def _template(self) -> str:
        """The template for the help text."""
        template = ""
        if title := getattr(self.app, "HELP_TITLE", ""):
            template += f"# {cleandoc(title)}\n\n"
        template += "{context_help}\n\n"
        if about := getattr(self.app, "HELP_ABOUT", ""):
            template += f"## About\n\n{cleandoc(about)}\n\n"
        if license := getattr(self.app, "HELP_LICENSE", ""):
            template += f"## License\n\n{cleandoc(license)}\n"
        return template

    def compose(self) -> ComposeResult:
        """Compose the layout of the help screen."""
        with Vertical() as help_screen:
            help_screen.border_title = "Help"
            with VerticalScroll():
                yield Markdown(self._template.format(context_help=self._context_help))
            with Center():
                yield Button(add_key("Okay", "Esc", self))

    @on(Button.Pressed)
    def action_close(self) -> None:
        """Close the help screen."""
        self.dismiss(None)

    @on(Markdown.LinkClicked)
    def visit(self, event: Markdown.LinkClicked) -> None:
        """Visit any link clicked in the help."""
        open_url(event.href)


### help.py ends here
