import unittest
from Q04_palindrome_permutation import is_palindrome_permutation


class palindrome_permutation_test(unittest.TestCase):
    def test_palindrome_permutation(self):
        self.assertEqual(True, is_palindrome_permutation("acbbac"))
        self.assertEqual(False, is_palindrome_permutation("asdasdsa"))


if __name__ == "__main__":
    unittest.main()
