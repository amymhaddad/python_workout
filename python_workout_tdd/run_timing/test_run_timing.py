from float import reduce_floats, add_floats


# Exercise 1 - tests
def test_one_digit_before_and_after():
    assert reduce_floats(0.0, 1, 1) == '0.0'

def test_two_digits_before_and_after():
    assert reduce_floats(1234.5678, 2, 3) == '34.567'

def test_three_digits_before_and_after():
    assert reduce_floats(1234.5678, 4, 3) == '1234.567'


# Exercise 2 - tests
def test_add_two_floats():
    assert add_floats("0.1", "0.2") == 0.3
