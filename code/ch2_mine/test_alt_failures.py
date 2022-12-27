from ast import main
import pytest
from cards import Card


def test_equality_fail():
    c1 = Card("asdf", "Rob", "todo", 5)
    c2 = Card("asdf", 3, "todo", 5)
    if c1 != c2:
        pytest.fail("cards are not equal")


def test_exception_fail():
    c1 = Card("asdf", "Rob", "todo", 5)
    c2 = Card("asdf", 3, "todo", 5)
    if c1 != c2:
        raise Exception("cards are not equal")


if __name__ == "__main__":
    test_equality_fail()
