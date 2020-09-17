import unittest


def flip_bits_to_win(n1, n2):
    c = n1 ^ n2
    count = 0

    while c:
        c &= c - 1
        count += 1

    return count


class Test(unittest.TestCase):
    def test_power_of_two(self):
        self.assertEqual(2, flip_bits_to_win(29, 15))
