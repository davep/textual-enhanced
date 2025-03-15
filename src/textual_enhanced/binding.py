"""Provides an enhanced binding class."""

##############################################################################
# Textual imports.
from textual.binding import Binding


##############################################################################
class HelpfulBinding(Binding):
    """A binding that should show in the help screen.

    In many cases a binding will be associated with a
    [`Command`][textual_enhanced.commands.Command] and will show up in the
    [help screen][textual_enhanced.dialogs.HelpScreen] anyway. But sometimes
    there will be bindings that are particular to a widget that I want
    highlighted, that I want called out in the help screen. On the other
    hand I don't want *all* bindings to show in the help screen as that
    would end up being a cluttered and unhelpful mess.

    This class lets a binding be marked as helpful, destined for the help
    screen.
    """

    @property
    def most_helpful_description(self) -> str:
        """The most helpful description possible."""
        return self.tooltip or self.description


### binding.py ends here
