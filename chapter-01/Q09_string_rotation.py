import unittest


def is_substring(s1, s2):
    return s1 in s2


def is_rotation(s1, s2):
    return is_substring(s1, s2 + s2)


class Test(unittest.TestCase):
    def test_string_rotate(self):
        self.assertEqual(True, is_rotation("erbottlewat", "waterbottle"))
        self.assertEqual(False, is_rotation("erbottletwa", "waterbottle"))
