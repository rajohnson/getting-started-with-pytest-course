import cards


def test_count_empty(cards_db):
    # given - the database is empty

    # when - count is called
    count = cards_db.count()

    # assert - count is  0
    assert 0 == count


def test_count_one_item(cards_db):
    # given - the database has one entry
    cards_db.add_card(cards.Card("task name"))

    # when - count is called
    count = cards_db.count()

    # assert - count is  1
    assert 1 == count
