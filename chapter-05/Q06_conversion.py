import unittest


def conversion(n1, n2):
    c = n1 ^ n2
    count = 0

    while c:
        c &= c - 1
        count += 1

    return count


class Test(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(2, conversion(29, 15))
