import os
import unittest

from vistrings import strings

this_dir = os.path.dirname(os.path.realpath(__file__))

class TestStrings(unittest.TestCase):
    def test_get_all_strings(self):
        vi_strings = strings.get_vi_plaintext(os.path.join(this_dir, "strings.vi"))
        assert "Comment Contents" in vi_strings
        assert "Label Contents" in vi_strings
        assert "String Constant Contents" in vi_strings
        # assert "Array of String contents" in vi_strings TODO