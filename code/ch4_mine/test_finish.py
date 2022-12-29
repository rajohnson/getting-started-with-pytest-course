import cards
import pytest


@pytest.mark.parametrize("initial_state", ["todo", "in prog", "done"])
def test_finish(cards_db, initial_state):
    c = cards.Card("asdlafgl", state=initial_state)
    idx = cards_db.add_card(c)
    cards_db.finish(idx)
    card = cards_db.get_card(idx)
    state = card.state
    assert state == "done"
