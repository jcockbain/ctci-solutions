import unittest


def swap_numbers(a, b):
    a = a - b
    b = b + a
    a = b - a
    return (a, b)


def swap_numbers_2(a, b):
    a = a ^ b
    b = b ^ a
    a = b ^ a
    return (a, b)


class Test(unittest.TestCase):
    def test_swap_numbers(self):
        a = 5
        b = 12
        a, b = swap_numbers(a, b)
        self.assertEqual((12, 5), (a, b))

        a = 5
        b = 12
        a, b = swap_numbers_2(a, b)
        self.assertEqual((12, 5), (a, b))
