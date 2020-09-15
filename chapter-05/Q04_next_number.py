import unittest


def get_next_number(n):
    ones = get_ones(n)
    upper = n + 1
    lower = n - 1
    while get_ones(upper) != ones:
        upper += 1

    while get_ones(lower) != ones:
        lower -= 1

    return upper, lower


def get_ones(n):
    mask = 1 << 31
    res = 0
    while mask:
        if mask & n:
            res += 1
        mask >>= 1
    return res


class Test(unittest.TestCase):
    def test_get_next_number(self):
        self.assertEqual((16, 4), get_next_number(8))
