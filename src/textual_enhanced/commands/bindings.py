"""Provides helper code for dealing with bindings."""

##############################################################################
# Textual imports.
from typing import Iterator

from textual.app import App
from textual.binding import Binding
from textual.dom import DOMNode
from textual.screen import Screen

##############################################################################
# Local imports.
from .command import Command


##############################################################################
def all_keys_for(node: DOMNode, source: type[Command] | Binding) -> Iterator[str]:
    """Get all the keys for the given command or binding.

    Args:
        node: The node we're working from.
        source: The command or binding to get the keys for.

    Yields:
        The display names of all the keys for the command/binding.
    """
    for binding in (
        [source]
        if isinstance(source, Binding)
        else [
            binding.binding
            for binding in (
                node if isinstance(node, (App, Screen)) else node.screen
            ).active_bindings.values()
            if binding.binding.id == source.__name__
        ]
        or [source.binding()]
    ):
        for key in binding.key.split(","):
            yield node.app.get_key_display(Binding(key.strip(), ""))


##############################################################################
def primary_key_for(node: DOMNode, source: type[Command] | Binding) -> str:
    """Get the primary key for the given command or binding.

    Args:
        node: The node we're working from.
        source: The command or binding to get the keys for.

    Returns:
        The display name of the primary key for the command/binding.
    """
    return next(all_keys_for(node, source))


### bindings.py ends here
