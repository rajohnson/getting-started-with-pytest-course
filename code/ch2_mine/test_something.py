def test_pass():
    a = 1
    assert a == 1


def test_fail():
    a = (2, 1, 3)
    assert a == (1, 1, 1)


def test_fail2():
    a = (2, 1, 3)
    assert a == (2, 1, 3, 1)
