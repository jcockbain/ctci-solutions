import unittest


def insert(N, M, i, j):
    j_mask = ~0 << j + 1
    i_mask = 1 << i
    clear_mask = j_mask | i_mask
    N = N & clear_mask
    M <<= i
    return N | M


class Insertion(unittest.TestCase):
    def test_insertion_1(self):
        expected = 2124
        res = insert(2048, 19, 2, 6)
        self.assertEqual(expected, res)

    def test_insertion_2(self):
        expected = 96
        res = insert(64, 1, 5, 5)
        self.assertEqual(expected, res)
