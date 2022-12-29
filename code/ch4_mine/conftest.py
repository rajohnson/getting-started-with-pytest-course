import pytest
import cards


@pytest.fixture(scope="session")
def cards_db_working(tmp_path_factory):
    """
    Returns a connection to the cards db
    """
    db_path = tmp_path_factory.mktemp("db")
    db = cards.CardsDB(db_path)
    yield db
    db.close()


@pytest.fixture()
def cards_db(cards_db_working):
    """
    Returns a connection to an empty cards db
    """
    cards_db_working.delete_all()
    return cards_db_working
