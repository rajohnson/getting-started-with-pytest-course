import cards


def test_finish(cards_db):
    for initial_state in ["todo", "in progress", "done"]:
        c = cards.Card("asdlafgl", state=initial_state)
        idx = cards_db.add_card(c)
        cards_db.finish(idx)
        card = cards_db.get_card(idx)
        state = card.state
        assert state == "done"
