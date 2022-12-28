import pathlib
import pytest
from tempfile import TemporaryDirectory
import cards


@pytest.fixture(scope="session")
def cards_db_working():
    with TemporaryDirectory() as temp_dir:
        db_path = pathlib.Path(temp_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


@pytest.fixture()
def cards_db(cards_db_working):
    cards_db_working.delete_all()
    return cards_db_working
