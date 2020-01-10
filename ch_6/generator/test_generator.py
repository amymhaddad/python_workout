from generator import myxml


def test_one_argument():
    assert myxml("foo") == "<foo></foo>"


def test_multiple_arguments():
    assert myxml("foo", "bar") == "<foo>bar</foo>"


def test_multiple_keyword_arguments():
    assert myxml("foo", "bar", a=1, b=2, c=3) == "<foo a='1' b='2' c='3'>bar</foo>"
