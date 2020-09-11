import unittest
from Q03_search_in_rotated_array import rotated_search


class RotatedSearchTest(unittest.TestCase):
    def test_rotated_search(self):
        array = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
        self.assertEqual(5, rotated_search(array, 1))

        array2 = [1, 2, 3, 4, 5]
        self.assertEqual(3, rotated_search(array2, 4))

        array3 = [5, 6, 7, 8, 1, 2, 3]
        self.assertEqual(2, rotated_search(array3, 7))

        array4 = [5, 5, 5, 6, 7, 8, 1, 2, 3]
        self.assertEqual(3, rotated_search(array4, 6))
