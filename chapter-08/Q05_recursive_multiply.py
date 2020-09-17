import unittest


def recursive_multiply(a, b):
    if a > b:
        return recursive_multiply_helper(b, a)
    return recursive_multiply_helper(a, b)


def recursive_multiply_helper(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger

    s = smaller >> 1

    half_product = recursive_multiply_helper(s, bigger)
    if smaller % 2 == 0:
        return half_product + half_product
    return half_product + half_product + bigger


class Test(unittest.TestCase):
    def test_recursive_multiply(self):
        self.assertEqual(42, recursive_multiply(6, 7))
        self.assertEqual(21, recursive_multiply(3, 7))
        self.assertEqual(100, recursive_multiply(10, 10))
