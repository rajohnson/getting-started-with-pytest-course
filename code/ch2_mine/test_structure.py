"""
Test structure for testing:
given -> when -> then
or 
arrange -> act -> assert
"""
from cards import Card


def test_to_dict():
    # given - a card
    c = Card("asdf", "Rob", "todo", 5)

    # when - to dict is called
    c_dict = c.to_dict()

    # assert - the dict from card will equal the manual dict
    expected_content = {
        "summary": "asdf",
        "owner": "Rob",
        "state": "todo",
        "id": 5,
    }
    assert expected_content == c_dict
