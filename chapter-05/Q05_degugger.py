import unittest


def is_power_of_two(n):
    return n & (n - 1) == 0


class Test(unittest.TestCase):
    def test_power_of_two(self):
        self.assertEqual(True, is_power_of_two(2))
        self.assertEqual(True, is_power_of_two(8))
        self.assertEqual(True, is_power_of_two(16))
        self.assertEqual(True, is_power_of_two(128))

        self.assertEqual(False, is_power_of_two(253))
        self.assertEqual(False, is_power_of_two(92))
        self.assertEqual(False, is_power_of_two(67))
        self.assertEqual(False, is_power_of_two(91))
