def test_cube():
    # given - number
    num = 42
    # when - it is cubed
    cube = num**3
    # assert - cube is equal to n*n*n
    assert cube == num * num * num
