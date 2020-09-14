from collections import Counter
import unittest


def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1

    return len([x for x in counter if counter[x] != 0]) == 0


class Test(unittest.TestCase):
    def test_is_unique(self):
        self.assertEqual(True, is_permutation("aabbd", "baabd"))
        self.assertEqual(False, is_permutation("abcdea", "abcde"))
        self.assertEqual(False, is_permutation("abcdefg", "acbdegi"))


if __name__ == "__main__":
    unittest.main()
