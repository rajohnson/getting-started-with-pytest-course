import cards
import pytest


@pytest.fixture(params=["todo", "in prog", "done"])
def initial_state(request):
    return request.param


@pytest.fixture(params=["asdf", "qwer", "zxcv"])
def initial_summary(request):
    return request.param


def test_finish(cards_db, initial_state, initial_summary):
    c = cards.Card(initial_summary, state=initial_state)
    idx = cards_db.add_card(c)
    cards_db.finish(idx)
    card = cards_db.get_card(idx)
    state = card.state
    assert state == "done"
