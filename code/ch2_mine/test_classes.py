from cards import Card


class TestEquality:
    def test_equality(self):
        c1 = Card("asdf", "Rob", "todo", 5)
        c2 = Card("asdf", "Rob", "todo", 5)
        assert c1 == c2
        assert c1 is not c2

    def test_equality_different_ids(self):
        c1 = Card("asdf", "Rob", "todo", 5)
        c2 = Card("asdf", "Rob", "todo", 22345265)
        assert c1 == c2
        assert c1 is not c2

    def test_inequality(self):
        c1 = Card("asdf", "Rob", "todo", 5)
        c2 = Card("dfhjsdry", "Rob", "todo", 22345265)
        assert c1 != c2
        assert c1 is not c2

    def test_inequality_same_id(self):
        c1 = Card("asdf", "Rob", "todo", 5)
        c2 = Card("dfhjsdry", "Rob", "todo", 5)
        assert c1 != c2
        assert c1 is not c2
