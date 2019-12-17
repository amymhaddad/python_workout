from pig_latin import secret_word


def test_word_starts_with_vowel():
    assert secret_word("air") == "airway"


def test_word_starts_with_consonant():
    assert secret_word("python") == "ythonpay"
