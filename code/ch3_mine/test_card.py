import pathlib
from tempfile import TemporaryDirectory
import cards


def test_count_empty():
    # given - the database is empty
    with TemporaryDirectory() as temp_dir:
        db_path = pathlib.Path(temp_dir)
        db = cards.CardsDB(db_path)

        # when - count is called
        count = db.count()

        # teardown
        db.close()

        # assert - count is  0
        assert 0 == count


def test_count_one_item():
    # given - the database has one entry
    with TemporaryDirectory() as temp_dir:
        db_path = pathlib.Path(temp_dir)
        db = cards.CardsDB(db_path)
        db.add_card(cards.Card("task name"))

        # when - count is called
        count = db.count()

        # teardown
        db.close()

        # assert - count is  1
        assert 1 == count
