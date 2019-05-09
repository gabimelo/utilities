from utils import compose


def inc_by_one(a):
    return a + 1


def mult_by_two(a):
    return a * 2


class TestUtils(object):
    def test_compose(self):
        assert compose(inc_by_one, mult_by_two)(3) == 8
