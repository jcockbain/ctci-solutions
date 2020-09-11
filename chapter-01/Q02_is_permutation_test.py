import unittest
from Q02_is_permutation import is_permutation


class Test(unittest.TestCase):
    def test_is_unique(self):
        self.assertEqual(True, is_permutation("aabbd", "baabd"))
        self.assertEqual(False, is_permutation("abcdea", "abcde"))
        self.assertEqual(False, is_permutation("abcdefg", "acbdegi"))


if __name__ == "__main__":
    unittest.main()
