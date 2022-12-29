import cards


def test_finish_in_progress(cards_db):
    c = cards.Card("asdlafgl", state="in progress")
    idx = cards_db.add_card(c)
    cards_db.finish(idx)
    card = cards_db.get_card(idx)
    state = card.state
    assert state == "done"


def test_finish_todo(cards_db):
    c = cards.Card("asdlafgl", state="todo")
    idx = cards_db.add_card(c)
    cards_db.finish(idx)
    card = cards_db.get_card(idx)
    state = card.state
    assert state == "done"


def test_finish_done(cards_db):
    c = cards.Card("asdlafgl", state="done")
    idx = cards_db.add_card(c)
    cards_db.finish(idx)
    card = cards_db.get_card(idx)
    state = card.state
    assert state == "done"
