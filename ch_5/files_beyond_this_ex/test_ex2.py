from ex_2 import get_multiples


def test_multiples_as_values():
    string = "4, 2"
    numbers = {(1, 2): [], (1, 4): []}
    assert get_multiples(numbers, string) == {(1, 2): [2], (1, 4): [4]}
