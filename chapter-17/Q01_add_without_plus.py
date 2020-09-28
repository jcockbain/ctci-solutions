import unittest


def add_without_plus(a, b):
    if b == 0:
        return a
    s = a ^ b
    carry = (a & b) << 1
    return add_without_plus(s, carry)


class Test(unittest.TestCase):
    def test_add_without_plus(self):
        self.assertEqual(12, add_without_plus(8, 4))
        self.assertEqual(13, add_without_plus(6, 7))
        self.assertEqual(6, add_without_plus(3, 3))
        self.assertEqual(7, add_without_plus(3, 4))
        self.assertEqual(90, add_without_plus(60, 30))
        self.assertEqual(-30, add_without_plus(-60, 30))
