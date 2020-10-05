import unittest


def missing_one(arr, n):
    expected_sum = n * (n + 1) / 2
    return expected_sum - sum(arr)


def missing_two(arr, n):
    expected_sum = n * (n + 1) / 2

    expected_product = 1
    for i in range(1, n + 1):
        expected_product *= i

    actual_product = 1
    for x in arr:
        actual_product *= x

    c = expected_sum - sum(arr)
    d = expected_product / actual_product

    # quadratic formula to solve equation
    a = (c - (c ** 2 - (4 * d)) ** 0.5) / 2

    b = c - a
    return (int(a), int(b))


class Test(unittest.TestCase):
    def test_missing_one(self):
        self.assertEqual(3, missing_one([1, 2, 4, 5], 5))
        self.assertEqual(1, missing_one([2, 3, 4, 5], 5))
        self.assertEqual(10, missing_one([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))

        self.assertEqual((3, 10), missing_two([1, 2, 4, 5, 6, 7, 8, 9], 10))
        self.assertEqual((1, 3), missing_two([2, 4, 5], 5))
