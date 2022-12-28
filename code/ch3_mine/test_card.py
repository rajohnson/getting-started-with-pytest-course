import pathlib
from tempfile import TemporaryDirectory
import cards


def test_empty():
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
