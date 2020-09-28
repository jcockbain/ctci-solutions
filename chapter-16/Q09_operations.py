import unittest


def multiply(a, b):
    res = 0
    for _ in range(abs(b)):
        res += abs(a)
    negative_count = sum([x < 0 for x in [a, b]])
    return negate(res) if negative_count == 1 else res


def divide(a, b):
    abs_a, abs_b = abs(a), abs(b)
    product, res = 0, 0
    negative_count = sum([x < 0 for x in [a, b]])
    while product < abs_a:
        product += abs_b
        res += 1

    return negate(res) if negative_count == 1 else res


def negate(n):
    new_sign = 1 if n < 0 else -1
    new_val = 0
    while n != 0:
        n += new_sign
        new_val += new_sign
    return new_val


def subtract(a, b):
    return a + negate(b)


class Test(unittest.TestCase):
    def test_operations(self):
        self.assertEqual(-20, negate(20))
        self.assertEqual(65, subtract(85, 20))
        self.assertEqual(65, multiply(5, 13))
        self.assertEqual(65, multiply(-5, -13))
        self.assertEqual(-65, multiply(-5, 13))
        self.assertEqual(-65, multiply(5, -13))
        self.assertEqual(3, divide(6, 2))
        self.assertEqual(3, divide(12, 4))
        self.assertEqual(-9, divide(-81, 9))
        self.assertEqual(-9, divide(81, -9))
        self.assertEqual(9, divide(-81, -9))
