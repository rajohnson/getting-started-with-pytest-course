from cards import Card


def test_field_access():
    c = Card("word", "Rob", "todo", 2)
    assert c.summary == "word"
    assert c.owner == "Rob"
    assert c.state == "todo"
    assert c.id == 2


def test_empty():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None


def test_equality():
    c1 = Card("asdf", "Rob", "todo", 5)
    c2 = Card("asdf", "Rob", "todo", 5)
    assert c1 == c2
    assert c1 is not c2


def test_equality_different_ids():
    c1 = Card("asdf", "Rob", "todo", 5)
    c2 = Card("asdf", "Rob", "todo", 22345265)
    assert c1 == c2
    assert c1 is not c2


def test_inequality():
    c1 = Card("asdf", "Rob", "todo", 5)
    c2 = Card("dfhjsdry", "Rob", "todo", 22345265)
    assert c1 != c2
    assert c1 is not c2


def test_inequality_same_id():
    c1 = Card("asdf", "Rob", "todo", 5)
    c2 = Card("dfhjsdry", "Rob", "todo", 5)
    assert c1 != c2
    assert c1 is not c2


def test_from_dict():
    c1 = Card("asdf", "Rob", "todo", 5)
    c2 = Card.from_dict(
        {"summary": "asdf", "owner": "Rob", "state": "todo", "id": 5}
    )
    assert c1 == c2
    assert c1 is not c2


def test_to_dict():
    card_content = {
        "summary": "asdf",
        "owner": "Rob",
        "state": "todo",
        "id": 5,
    }
    c = Card("asdf", "Rob", "todo", 5)
    assert card_content == c.to_dict()
