import unittest


def trailing_zeroes(n):
    res = 0
    i = 5
    while i <= n:
        res += n // i
        i *= 5
    return res


class Test(unittest.TestCase):
    def test_trailing_zeroes(self):
        self.assertEqual(0, trailing_zeroes(3))
        self.assertEqual(10, trailing_zeroes(45))
