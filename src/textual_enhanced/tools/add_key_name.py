"""Provides a function for adding a key name to a label."""

##############################################################################
# Python imports.
from typing import Any

##############################################################################
# Textual imports.
from textual.app import App
from textual.widget import Widget


##############################################################################
def add_key(label: str, key: str, context: App[Any] | Widget | None = None) -> str:
    """Add a key name to a label.

    Args:
        label: The label to add the key to.
        key: The display name of the key to add.
        context: The widget, screen or application.

    Returns:
        The label with a display of the key added.

    Notes:
        By default the key label will use the current theme's accent colour,
        if that can't be derived from the context them `dim` will be used.
    """
    if isinstance(context, Widget):
        context = context.app
    key_colour = (
        "dim"
        if context is None or context.current_theme is None
        else context.current_theme.accent
    )
    return f"{label} [{key_colour}]\\[{key}][/]"


### add_key_name.py ends here
