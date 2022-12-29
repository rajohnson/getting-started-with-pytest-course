import cards
import pytest


@pytest.fixture(params=["todo", "in prog", "done"])
def initial_state(request):
    return request.param


@pytest.mark.parametrize("summary", ["asdf", "qwer", "zxcv"])
def test_finish(cards_db, initial_state, summary):
    c = cards.Card(summary, state=initial_state)
    idx = cards_db.add_card(c)
    cards_db.finish(idx)
    card = cards_db.get_card(idx)
    state = card.state
    assert state == "done"
