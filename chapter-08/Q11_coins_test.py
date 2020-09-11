import unittest
from Q11_coins import change_possibilities


class CoinsTest(unittest.TestCase):
    def test_coin_test(self):
        actual = change_possibilities(50, [5, 10])
        expected = 6
        self.assertEqual(expected, actual)
