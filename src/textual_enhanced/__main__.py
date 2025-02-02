"""A simple demo app of some of the enhancements."""

##############################################################################
# Textual imports.
from textual import on, work
from textual.app import ComposeResult
from textual.widgets import Button, Footer, Header

##############################################################################
# Textual Enhanced imports.
from textual_enhanced import __version__
from textual_enhanced.app import EnhancedApp
from textual_enhanced.commands import Command, CommonCommands, Help, Quit
from textual_enhanced.dialogs import Confirm, HelpScreen, ModalInput


##############################################################################
class DemoApp(EnhancedApp[None]):
    """A little demo app."""

    HELP_TITLE = f"textual-enhanced v{__version__}"
    HELP_ABOUT = "A library of mildly-opinionated enhancements to Textual."
    HELP_LICENSE = """MIT License

    Copyright (c) 2025 Dave Pearson <davep@davep.org>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to
    deal in the Software without restriction, including without limitation the
    rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
    sell copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
    IN THE SOFTWARE.
    """

    COMMAND_MESSAGES = {Help, Quit}
    COMMANDS = {CommonCommands}
    BINDINGS = Command.bindings(*COMMAND_MESSAGES)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Button("Quick input", id="input")
        yield Button("Yes or no?", id="confirm")
        yield Footer()

    @on(Button.Pressed, "#input")
    @work
    async def input_action(self) -> None:
        if text := await self.push_screen_wait(
            ModalInput(placeholder="Enter some text here")
        ):
            self.notify(f"Entered '{text}")

    @on(Button.Pressed, "#confirm")
    @work
    async def confirm_action(self) -> None:
        self.notify(
            "YES!"
            if await self.push_screen_wait(
                Confirm(
                    "Well?", "So, what's the decision? Are we going with yes or no?"
                )
            )
            else "No!"
        )

    @on(Help)
    def action_help_command(self) -> None:
        self.push_screen(HelpScreen())

    @on(Quit)
    def action_quit_command(self) -> None:
        self.exit()


##############################################################################
if __name__ == "__main__":
    DemoApp().run()

### __main__.py ends here
