"""A simple demo app of some of the enhancements."""

##############################################################################
# Python imports.
from dataclasses import dataclass

##############################################################################
# Textual imports.
from textual import on, work
from textual.app import ComposeResult, RenderResult
from textual.containers import Horizontal
from textual.message import Message
from textual.widgets import Button, Footer, Header

##############################################################################
# Textual Enhanced imports.
from textual_enhanced import __version__
from textual_enhanced.app import EnhancedApp
from textual_enhanced.binding import HelpfulBinding
from textual_enhanced.commands import (
    ChangeTheme,
    Command,
    CommandHit,
    CommandHits,
    CommandsProvider,
    CommonCommands,
    Help,
    Quit,
)
from textual_enhanced.dialogs import Confirm, ModalInput
from textual_enhanced.screen import EnhancedScreen


##############################################################################
@dataclass
class ShowNumber(Message):
    number: int


##############################################################################
class NumberProvider(CommandsProvider):
    def commands(self) -> CommandHits:
        for n in range(500):
            yield CommandHit(
                f"This is the rather special and unique number {n}",
                f"This is some help about the number {n}, just in case you needed it",
                ShowNumber(n),
            )


##############################################################################
class SayOne(Command):
    ACTION = "say('One')"


##############################################################################
class SayTwo(Command):
    ACTION = "say('Two')"


##############################################################################
class OtherCommands(CommandsProvider):
    def commands(self) -> CommandHits:
        yield SayOne()
        yield SayTwo()


##############################################################################
class HelpfulButton(Button):
    BINDINGS = [
        HelpfulBinding("ctrl+o", "gndn", description="This does nothing useful")
    ]


##############################################################################
class Ruler(Horizontal):
    DEFAULT_CSS = """
    Ruler {
        width: 1fr;
        height: 1;
        text-align: center;
    }
    """

    def render(self) -> RenderResult:
        return "----- | -----"


##############################################################################
class Main(EnhancedScreen[None]):
    TITLE = "Title"
    SUB_TITLE = "Title"
    COMMAND_MESSAGES = (Help, ChangeTheme, Quit)
    COMMANDS = {CommonCommands, OtherCommands}
    BINDINGS = Command.bindings(
        *COMMAND_MESSAGES,
        HelpfulBinding(
            "ctrl+y, ctrl+i",
            "gndn",
            show=False,
            description="This is the description",
            tooltip="This is the tooltip",
        ),
        HelpfulBinding("ctrl+t, ctrl+k", "gndn", description="This is the description"),
    )
    HELP = "Here's some really long text to scroll: {}".format(
        "\n".join([f"{n}. This is a filler line" for n in range(100)])
    )

    def compose(self) -> ComposeResult:
        yield Header()
        yield Ruler()
        yield HelpfulButton("Quick input", id="input")
        yield Button("Another input", id="input_with_default")
        yield Button("Yes or no?", id="confirm")
        yield Button("Pick a number", id="number")
        yield Footer()

    @on(Button.Pressed, "#input, #input_with_default")
    @work
    async def input_action(self, message: Button.Pressed) -> None:
        if text := await self.app.push_screen_wait(
            ModalInput(placeholder="Enter some text here")
            if message.button.id == "input"
            else ModalInput(
                placeholder="This has an initial value", initial="Testing..."
            )
        ):
            self.notify(f"Entered '{text}")

    @on(Button.Pressed, "#confirm")
    @work
    async def confirm_action(self) -> None:
        self.notify(
            "YES!"
            if await self.app.push_screen_wait(
                Confirm(
                    "Well?", "So, what's the decision? Are we going with yes or no?"
                )
            )
            else "No!"
        )

    @on(Button.Pressed, "#number")
    def pick_a_number(self) -> None:
        self.show_palette(NumberProvider)

    @on(ShowNumber)
    def show_the_number(self, number: ShowNumber) -> None:
        self.notify(f"You picked {number.number}")

    def action_say(self, text: str) -> None:
        self.notify(text)


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

    COMMANDS = set()

    def get_default_screen(self) -> Main:
        return Main()

    def on_mount(self) -> None:
        self.update_keymap({"Help": "f7,f1,h,question_mark"})


##############################################################################
if __name__ == "__main__":
    DemoApp().run()

### __main__.py ends here
