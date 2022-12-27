from cards import Card


def test_equality_fail():
    c1 = Card("asdf", "Rob", "todo", 5)
    c2 = Card("asdf", 3, "todo", 5)
    assert c1 == c2


if __name__ == "__main__":
    test_equality_fail()
