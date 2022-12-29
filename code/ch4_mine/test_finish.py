import cards


def test_finish(cards_db):
    c = cards.Card("asdlafgl", state="in progress")
    idx = cards_db.add_card(c)
    cards_db.finish(idx)
    card = cards_db.get_card(idx)
    state = card.state
    assert state == "done"
