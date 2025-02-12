"""A modal screen for quickly getting an input value."""

##############################################################################
# Textual imports.
from textual import on
from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Input


##############################################################################
class ModalInput(ModalScreen[str | None]):
    """A modal screen to get input from the user."""

    CSS = """
    ModalInput {
        align: center middle;

        Input, Input:focus {
            border: round $border;
            width: 60%;
            padding: 1;
            height: auto;
        }
    }
    """

    BINDINGS = [("escape", "escape")]

    def __init__(
        self,
        placeholder: str | None = None,
        initial: str = "",
        classes: str | None = None,
    ) -> None:
        """Initialise the object.

        Args:
            placeholder: The placeholder text to use.
            initial: The initial value for the input.
            classes: The CSS classes of the modal input.
        """
        super().__init__(classes=classes)
        self._placeholder = placeholder or ""
        """The placeholder to use for the input."""
        self._initial = initial
        """The initial value for the input."""

    def compose(self) -> ComposeResult:
        """Compose the input dialog."""
        yield Input(self._initial, placeholder=self._placeholder)

    @on(Input.Submitted)
    def search(self) -> None:
        """Accept the input."""
        self.dismiss(self.query_one(Input).value.strip())

    def action_escape(self) -> None:
        """Escape out without getting the input."""
        self.dismiss(None)


### modal_input.py ends here
