"""A simple demo app of some of the enhancements."""

##############################################################################
# Textual imports.
from textual.app import ComposeResult
from textual.widgets import Footer, Header

##############################################################################
# Textual Enhanced imports.
from textual_enhanced.app import EnhancedApp


##############################################################################
class DemoApp(EnhancedApp[None]):
    """A little demo app."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()


##############################################################################
if __name__ == "__main__":
    DemoApp().run()

### __main__.py ends here
