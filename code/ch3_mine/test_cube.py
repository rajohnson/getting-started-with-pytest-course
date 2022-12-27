import pytest


@pytest.fixture()
def num():
    return 42


def test_cube(num):
    # given - number
    # when - it is cubed
    cube = num**3
    # assert - cube is equal to n*n*n
    assert cube == num * num * num
