import unittest

from Q01_insertion import insert


class Insertion(unittest.TestCase):
    def test_insertion_1(self):
        expected = 2124
        res = insert(2048, 19, 2, 6)
        self.assertEqual(expected, res)

    def test_insertion_2(self):
        expected = 96
        res = insert(64, 1, 5, 5)
        self.assertEqual(expected, res)
