from src.helpers import remove_extra_spaces


class TestRemoveExtraSpaces:
    accepted_string = "This is a test example"

    def test_multiple_spaces(self):
        multiple_spaces = "This  is a    test   example"
        res = remove_extra_spaces(multiple_spaces)
        assert self.accepted_string == res

    def test_multiple_newlines(self):
        multiple_spaces = "This    \n is a test \n \n example"
        res = remove_extra_spaces(multiple_spaces)
        assert self.accepted_string == res

    def test_multiple_tabs(self):
        multiple_spaces = "This \t\t is a \t test \t example"
        res = remove_extra_spaces(multiple_spaces)
        assert self.accepted_string == res

    def test_multiple_whitespace_characters(self):
        multiple_spaces = "This \t is \n     a \t test \n example"
        res = remove_extra_spaces(multiple_spaces)
        assert self.accepted_string == res
