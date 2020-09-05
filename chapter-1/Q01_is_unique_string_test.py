import unittest
from Q01_is_unique_string import is_unique


class Test(unittest.TestCase):
    def test_is_unique(self):
        self.assertEqual(False, is_unique("aabbd"))
        self.assertEqual(False, is_unique("abcdea"))
        self.assertEqual(True, is_unique("abcdefg"))


if __name__ == "__main__":
    unittest.main()
