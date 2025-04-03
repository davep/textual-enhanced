"""Provides enhanced container classes."""

##############################################################################
# Python imports.
from typing import Literal

##############################################################################
# Textual imports.
from textual.containers import VerticalScroll

##############################################################################
# Local imports.
from .binding import HelpfulBinding


##############################################################################
class EnhancedVerticalScroll(VerticalScroll):
    """A vertical scroll container with some enhancements.

    The main purpose of this class is to add some extra bindings for
    scrolling, and to add a couple more scrolling actions.
    """

    BINDINGS = [
        HelpfulBinding("j, e, enter", "scroll_down", tooltip="Scroll down one line"),
        HelpfulBinding("k, y", "scroll_up", tooltip="Scroll up one line"),
        HelpfulBinding("f, space, z", "page_down", tooltip="Scroll down one page"),
        HelpfulBinding("b, w", "page_up", tooltip="Scroll up one page"),
        HelpfulBinding(
            "shift+pageup, u", "scroll_half_page(-1)", tooltip="Scroll up half a page"
        ),
        HelpfulBinding(
            "shift+pagedown, d",
            "scroll_half_page(1)",
            tooltip="Scroll down half a page",
        ),
        HelpfulBinding("g, <, p, %", "scroll_home", tooltip="Scroll to the top"),
        HelpfulBinding("G, >", "scroll_end", tooltip="Scroll to the bottom"),
    ]
    """Additional movement bindings that might help vim/less users."""

    def action_scroll_half_page(self, direction: Literal[-1, 1]) -> None:
        """Scroll the view half a page in the given direction.

        Args:
            direction: The direction to scroll in.
        """
        self.scroll_relative(y=(self.size.height // 2) * direction)


### containers.py ends here
