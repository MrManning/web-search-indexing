from collections import Counter
from src.helpers import remove_extra_spaces, remove_punctuation, remove_digits, remove_stopwords

accepted_string = "This is a test example"


def test_multiple_spaces():
    multiple_spaces = "This  is a    test   example"
    result = remove_extra_spaces(multiple_spaces)

    assert result == accepted_string


def test_multiple_newlines():
    multiple_spaces = "This    \n is a test \n \n example"
    result = remove_extra_spaces(multiple_spaces)

    assert result == accepted_string


def test_multiple_tabs():
    multiple_spaces = "This \t\t is a \t test \t example"
    result = remove_extra_spaces(multiple_spaces)

    assert result == accepted_string


def test_multiple_whitespace_characters():
    multiple_spaces = "This \t is \n     a \t test \n example"
    result = remove_extra_spaces(multiple_spaces)

    assert result == accepted_string


def test_remove_punctuation():
    multiple_punctuation = [".", "a", "£30", "{", "t!st", "{example}"]
    result = remove_punctuation(multiple_punctuation)
    accepted_list = ["a", "{example}", "£30", "t!st"]

    assert Counter(result) == Counter(accepted_list)


def test_remove_digits():
    multiple_digits = ["30", "2004-12", "a number 42", "test", "empty", "2020"]
    result = remove_digits(multiple_digits)
    accepted_list = ["2004-12", "a number 42", "empty", "test"]

    assert Counter(result) == Counter(accepted_list)


def test_remove_stopwords():
    multiple_stopwords = ["the", "test", "example", "and"]
    result = remove_stopwords(multiple_stopwords)
    accepted_list = ["test", "example"]

    assert Counter(result) == Counter(accepted_list)