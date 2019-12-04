from sum_numbers import mysum, list_average, word_length, sum_ints

# EXERCISE 1 tests
def test_sum_one_number_no_start_value():
    assert mysum([1]) == 1


def test_sum_multiple_numbers_no_start_value():
    assert mysum([1, 2, 3]) == 6


def test_sum_one_number_with_start_value():
    assert mysum([1], 1) == 2


def test_sum_multiple_numbers_with_start_value():
    assert mysum([1, 2, 3], 4) == 10


# EXERCISE 2 tests


def test_average():
    assert list_average([1, 2, 3]) == 2


# EXERCISE 3 tests


def test_return_empty_list():
    assert word_length(["", "", ""]) == (0, 0, 0)


def test_list_with_various_word_lengths():
    assert word_length(["a", "of", "her"]) == (1, 3, 2)


def test_list_with_same_word_lengths():
    assert word_length(["a", "a", "a", "her"]) == (1, 3, 1)


# EXERCISE 4 tests
def test_sum_list_of_integers():
    assert sum_ints([10, 10, 10]) == 30


def test_sum_list_with_words():
    assert sum_ints([10, 10, "word", 10]) == 30


def test_sum_list_with_ints_and_strings_with_numbers():
    assert sum_ints(["20", "20", 20]) == 60


def test_random_list():
    assert sum_ints([10, "10", "word", 10, "!!"]) == 30
