import unittest


def is_unique(string):
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

    return True


class Test(unittest.TestCase):
    def test_is_unique(self):
        self.assertEqual(False, is_unique("aabbd"))
        self.assertEqual(False, is_unique("abcdea"))
        self.assertEqual(True, is_unique("abcdefg"))

        self.assertEqual(False, is_unique("".join([chr(i) for i in range(129)])))
