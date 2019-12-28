from first_last import firstlast


def test_first_last_list():
    assert firstlast([1, 2, 3, 4]) == [1, 4]


def test_first_last_string():
    assert firstlast("abcd") == "ad"


def test_first_last_tuple():
    assert firstlast((1, 2, 3, 4)) == (1, 4)
