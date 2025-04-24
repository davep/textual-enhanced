"""Provides a history tracking class."""

##############################################################################
# Python imports.
from collections import deque
from typing import Generic, Iterator, Sequence, TypeVar

##############################################################################
# Textual imports.
from textual.geometry import clamp

##############################################################################
# Typing extensions imports.
from typing_extensions import Self

##############################################################################
HistoryItem = TypeVar("HistoryItem")
"""The type of an item in history."""


##############################################################################
class History(Generic[HistoryItem]):
    """A class for handling and tracking history."""

    def __init__(
        self, history: Sequence[HistoryItem] | None = None, max_length: int = 500
    ) -> None:
        """Initialise the history object.

        Args:
            history: Set to the given history.
            max_length: Optional maximum length for the history.
        """
        self._history: deque[HistoryItem] = deque(history or [], maxlen=max_length)
        """The history."""
        self._current = max(len(self._history) - 1, 0)
        """The current location within the history."""

    @property
    def current_location(self) -> int | None:
        """The current integer location in the history.

        If there is no valid location the value is `None`.
        """
        try:
            _ = self._history[self._current]
        except IndexError:
            return None
        return self._current

    @property
    def current_item(self) -> HistoryItem | None:
        """The current item in the history.

        If there is no current item in the history the value is `None`.
        """
        try:
            return self._history[self._current]
        except IndexError:
            return None

    @property
    def can_go_backward(self) -> bool:
        """Can history go backward?"""
        return bool(self._current)

    def backward(self) -> bool:
        """Go backward through the history.

        Returns:
            `True` if we moved through history, `False` if not.
        """
        if self.can_go_backward:
            self._current -= 1
            return True
        return False

    @property
    def can_go_forward(self) -> bool:
        """Can history go forward?"""
        return self._current < len(self._history) - 1

    def forward(self) -> bool:
        """Go forward through the history.

        Returns:
            `True` if we moved through history, `False` if not.
        """
        if self.can_go_forward:
            self._current += 1
            return True
        return False

    def goto(self, location: int) -> Self:
        """Jump to a specific location within history."""
        self._current = clamp(location, 0, len(self._history) - 1)
        return self

    def goto_end(self) -> Self:
        """Go to the end of the history."""
        self.goto(len(self) - 1)
        return self

    def add(self, item: HistoryItem) -> Self:
        """Add an item to the history.

        Args:
            item: The item to add.

        Returns:
            Self.
        """
        self._history.append(item)
        return self.goto_end()

    def __len__(self) -> int:
        """The length of the history."""
        return len(self._history)

    def __iter__(self) -> Iterator[HistoryItem]:
        """Support iterating through the history."""
        return iter(self._history)

    def __delitem__(self, index: int) -> None:
        """Delete an item in history."""
        del self._history[index]


### history.py ends here
