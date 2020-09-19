import unittest

EVEN = 0x5555555555555555
ODD = 0xAAAAAAAAAAAAAAAA


def pairwise_swap(n):
    return ((n & ODD) >> 1) | ((n & EVEN) << 1)


class Test(unittest.TestCase):
    def test_pairwise_swap(self):
        self.assertEqual(4, pairwise_swap(8))
        self.assertEqual(39, pairwise_swap(27))
