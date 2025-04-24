"""Test the history class."""

##############################################################################
# Python imports.
from typing import Sequence

##############################################################################
# Pytest imports.
from pytest import mark

##############################################################################
# Local imports.
from textual_enhanced.tools import History


##############################################################################
def test_empty_history_has_no_location() -> None:
    """An empty history object should have no location."""
    assert History().current_location is None


##############################################################################
def test_empty_history_has_no_item() -> None:
    """An empty history object should have no item."""
    assert History().current_item is None


##############################################################################
def test_empty_history_has_no_length() -> None:
    """An empty history object should have zero length."""
    assert len(History()) == 0


##############################################################################
def test_empty_history_has_nowhere_to_go() -> None:
    """An empty history should not be able to move."""
    assert History().can_go_backward is False
    assert History().can_go_forward is False


##############################################################################
@mark.parametrize("initial", ([1], [1, 2], range(100)))
def test_pre_populate_history_has_location(initial: Sequence[int]) -> None:
    """A pre-populated history should be at the last location."""
    assert History[int](initial).current_location == len(initial) - 1


##############################################################################
@mark.parametrize("initial", ([1], [1, 2], range(100)))
def test_pre_populate_history_has_an_item(initial: Sequence[int]) -> None:
    """A pre-populated history's item should be the last item."""
    assert History[int](initial).current_item == initial[-1]


##############################################################################
@mark.parametrize(
    "initial, expected",
    (
        ([1], 1),
        ([1, 2], 2),
        (range(100), 100),
        (range(200), 100),
    ),
)
def test_pre_populate_history_has_length(initial: Sequence[int], expected: int) -> None:
    """A pre-populated history should be the correct length."""
    assert len(History[int](initial, max_length=100)) == expected


##############################################################################
@mark.parametrize("values", ([1], [1, 2], range(100)))
def test_hand_populated_history_has_location(values: Sequence[int]) -> None:
    """A hand-populated history should end up at the last location."""
    history = History[int]()
    for value in values:
        history.add(value)
    assert history.current_location == len(values) - 1


##############################################################################
@mark.parametrize("values", ([1], [1, 2], range(100)))
def test_hand_populated_history_has_an_item(values: Sequence[int]) -> None:
    """A hand-populated history's item should be the last item."""
    history = History[int]()
    for value in values:
        history.add(value)
    assert history.current_item == values[-1]


##############################################################################
@mark.parametrize(
    "values, expected",
    (
        ([1], 1),
        ([1, 2], 2),
        (range(100), 100),
        (range(200), 100),
    ),
)
def test_hand_populated_history_has_length(
    values: Sequence[int], expected: int
) -> None:
    """A pre-populated history should be the correct length."""
    history = History[int](max_length=100)
    for value in values:
        history.add(value)
    assert len(history) == expected


##############################################################################
def test_backward() -> None:
    """We should be able to move backward through history until we can't."""
    history = History[int]([1, 2, 3])
    assert history.current_location == 2
    assert history.can_go_backward is True
    assert history.backward() is True
    assert history.current_location == 1
    assert history.can_go_backward is True
    assert history.backward() is True
    assert history.current_location == 0
    assert history.can_go_backward is False
    assert history.backward() is False
    assert history.current_location == 0


##############################################################################
def test_backward_empty() -> None:
    """We should not be able to go backward in an empty history."""
    history = History[None]([])
    assert history.current_location is None
    assert history.backward() is False
    assert history.current_location is None


##############################################################################
def test_forward() -> None:
    """We should be able to move forward through history until we can't."""
    history = History[int]([1, 2, 3])
    assert history.backward() is True
    assert history.backward() is True
    assert history.backward() is False
    assert history.can_go_backward is False
    assert history.current_location == 0
    assert history.can_go_forward is True
    assert history.forward() is True
    assert history.current_location == 1
    assert history.can_go_forward is True
    assert history.forward() is True
    assert history.current_location == 2
    assert history.can_go_forward is False
    assert history.forward() is False
    assert history.current_location == 2


##############################################################################
def test_forward_empty() -> None:
    """We should not be able to go forward in an empty history."""
    history = History[None]()
    assert history.current_location is None
    assert history.forward() is False
    assert history.current_location is None


##############################################################################
def test_iterator() -> None:
    """We should be able to use history as an iterator."""
    assert list(History[int]([1, 2, 3])) == [1, 2, 3]


##############################################################################
@mark.parametrize("desired, achieved", ((0, 0), (1, 1), (2, 2), (3, 2), (-1, 0)))
def test_goto(desired: int, achieved: int) -> None:
    """We should be able to go to specific locations in history."""
    assert History[None]((None, None, None)).goto(desired).current_location == achieved


##############################################################################
def test_goto_end() -> None:
    """We should be able to go to the end of the history."""
    history = History[None]((None,) * 100)
    assert history.goto(0).current_location == 0
    assert history.goto_end().current_location == 99


##############################################################################
def test_goto_end_of_nothing() -> None:
    """Going to the end when there is no history should cause no problem."""
    assert History[None]().goto_end().current_location is None


##############################################################################
def test_goto_empty() -> None:
    """Going to a location in an empty list should keep the location as `None`."""
    assert History[None]().goto(42).current_location is None


##############################################################################
def test_goto_and_movement_in_empty_history() -> None:
    """A combination of goto and movement in a empty history should be fine."""
    history = History[None]()
    assert history.current_location is None
    assert history.goto(42).current_location is None
    assert history.forward() is False
    assert history.current_location is None
    assert history.backward() is False
    assert history.current_location is None


##############################################################################
def test_delete_history() -> None:
    """We should be able to delete an item in history."""
    history = History[None]((None,))
    assert len(history) == 1
    del history[0]
    assert len(history) == 0


### test_history.py ends here
