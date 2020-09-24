import unittest


def number_max(a, b):
    diff = a - b
    k = 1 ^ ((diff >> 31) & 1)
    return (k * a) + ((1 ^ k) * b)


class Test(unittest.TestCase):
    def test_number_max(self):
        self.assertEqual(12, number_max(12, 8))
        self.assertEqual(8, number_max(-12, 8))
        self.assertEqual(100, number_max(100, -100))
        self.assertEqual(100, number_max(100, 0))
        self.assertEqual(100, number_max(100, 100))
