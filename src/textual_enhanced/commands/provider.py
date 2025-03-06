"""Provides a base command-oriented command palette provider class."""

##############################################################################
# Python imports.
from abc import abstractmethod
from functools import partial
from typing import Iterator, NamedTuple, TypeAlias

##############################################################################
# Rich imports.
from rich.text import Text

##############################################################################
# Textual imports.
from textual.command import DiscoveryHit, Hit, Hits, Provider
from textual.content import Content
from textual.message import Message

##############################################################################
# Local imports.
from .command import Command


##############################################################################
class CommandHit(NamedTuple):
    """A command hit for use in building a command palette hit."""

    command: str
    """The command."""
    description: str
    """The description of the command."""
    message: Message
    """The message to emit when the command is chosen."""


##############################################################################
CommandHits: TypeAlias = Iterator[CommandHit | Command]
"""The result of looking for commands to make into hits."""


##############################################################################
class CommandsProvider(Provider):
    """A base class for command-message-oriented command palette commands."""

    @classmethod
    def prompt(cls) -> str:
        """The prompt for the command provider."""
        return ""

    def maybe(self, command: type[Command]) -> CommandHits:
        """Yield a command if it's applicable.

        Args:
            command: The type of the command to maybe yield.

        Yields:
            The command if it can be used right now.

        This method takes the command, looks at its `action_name` and uses
        Textual's `check_action` to see if the action can be performed right
        now. If it can it will `yield` an instance of the command, otherwise
        it does nothing.
        """
        if self.screen.check_action(command.action_name(), ()):
            yield command()

    @abstractmethod
    def commands(self) -> CommandHits:
        """Provide the command data for the command palette.

        Yields:
            A tuple of the command, the command description and a command message.
        """
        raise NotImplementedError

    @property
    def _commands(self) -> Iterator[CommandHit]:
        """The commands available for the palette."""
        return (
            CommandHit(command.context_command, command.context_tooltip, command)
            if isinstance(command, Command)
            else command
            for command in self.commands()
        )

    def _maybe_add_binding(
        self, message: Command | Message, text: str | Text | Content
    ) -> Text | Content:
        """Maybe add binding details to some text.

        Args:
            message: The command message to maybe get the binding for.
            text: The text to add the binding details to.

        Returns:
            The resulting text.
        """
        if isinstance(text, str):
            text = Text(text)
        if not isinstance(message, Command) or not message.has_binding:
            return text
        key = Text(
            f"[{self.app.get_key_display(message.primary_binding())}]",
            style=(self.app.current_theme.accent if self.app.current_theme else None)
            or "dim",
        )
        # There's a breaking change between Textual 1.0 and 2.0
        # regarding how commands in the command palette are handled. I
        # could report it but I know the experience will be exhausting
        # and fruitless; so let's just handle it here.
        #
        # Eventually, once I'm happy that Textual 2.x is stable enough
        # to use, I'll tidy this up.
        if isinstance(text, Text):
            return text.append_text(Text(" ")).append_text(key)
        return Content.assemble(text, " ", Content.from_rich_text(key))  # type: ignore

    async def discover(self) -> Hits:
        """Handle a request to discover commands.

        Yields:
            Command discovery hits for the command palette.
        """
        for command, description, message in self._commands:
            yield DiscoveryHit(
                self._maybe_add_binding(message, command),
                partial(self.screen.post_message, message),
                help=description,
            )

    async def search(self, query: str) -> Hits:
        """Handle a request to search for commands that match the query.

        Args:
            query: The query from the user.

        Yields:
            Command hits for the command palette.
        """
        matcher = self.matcher(query)
        for command, description, message in self._commands:
            if match := matcher.match(command):
                yield Hit(
                    match,
                    self._maybe_add_binding(message, matcher.highlight(command)),
                    partial(self.screen.post_message, message),
                    help=description,
                )


### provider.py ends here
