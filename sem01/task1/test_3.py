from soap import checkText


def test_step1(good_word, bad_word):
    assert good_word in checkText(bad_word)
