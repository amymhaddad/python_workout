from sentence_pig_latin import convert_sentence


def test_short_sentence():
    assert (
        convert_sentence("this is a test translation")
        == "histay isway away esttay ranslationtay"
    )
