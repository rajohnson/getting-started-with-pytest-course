import pathlib
import pytest
from tempfile import TemporaryDirectory
import cards


@pytest.fixture(scope="module")
def cards_db_module():
    with TemporaryDirectory() as temp_dir:
        db_path = pathlib.Path(temp_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


@pytest.fixture()
def cards_db(cards_db_module):
    cards_db_module.delete_all()
    return cards_db_module


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
