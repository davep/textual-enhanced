"""A simple demo app of some of the enhancements."""

##############################################################################
# Textual imports.
from textual import on, work
from textual.app import ComposeResult
from textual.widgets import Button, Footer, Header

##############################################################################
# Textual Enhanced imports.
from textual_enhanced.app import EnhancedApp
from textual_enhanced.dialogs import ModalInput


##############################################################################
class DemoApp(EnhancedApp[None]):
    """A little demo app."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Button("Quick input")
        yield Footer()

    @on(Button.Pressed)
    @work
    async def demo_input(self) -> None:
        if text := await self.push_screen_wait(
            ModalInput(placeholder="Enter some text here")
        ):
            self.notify(f"Entered '{text}")


##############################################################################
if __name__ == "__main__":
    DemoApp().run()

### __main__.py ends here
