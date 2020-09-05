import unittest
from Q01_sorted_merge import sorted_merge


class Test(unittest.TestCase):
    def test_sorted_merge(self):
        a = [1, 2, None, None]
        b = [3, 4]
        sorted_merge(a, b)
        self.assertEqual(a, [1, 2, 3, 4])
