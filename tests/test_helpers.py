from collections import Counter
from src.helpers import remove_extra_spaces, remove_punctuation

accepted_string = "This is a test example"


def test_multiple_spaces():
    multiple_spaces = "This  is a    test   example"
    res = remove_extra_spaces(multiple_spaces)
    assert accepted_string == res


def test_multiple_newlines():
    multiple_spaces = "This    \n is a test \n \n example"
    res = remove_extra_spaces(multiple_spaces)
    assert accepted_string == res


def test_multiple_tabs():
    multiple_spaces = "This \t\t is a \t test \t example"
    res = remove_extra_spaces(multiple_spaces)
    assert accepted_string == res


def test_multiple_whitespace_characters():
    multiple_spaces = "This \t is \n     a \t test \n example"
    res = remove_extra_spaces(multiple_spaces)
    assert accepted_string == res


def test_remove_punctuation():
    multiple_punctuation = [".", "a", "£30", "{", "t!st", "{example}"]
    res = remove_punctuation(multiple_punctuation)
    accepted_list = ["a", "{example}", "£30", "t!st"]

    assert Counter(accepted_list) == Counter(res)
