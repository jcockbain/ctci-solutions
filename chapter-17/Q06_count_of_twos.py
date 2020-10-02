import unittest


def count_of_twos(n):
    res = 0

    for i in range(len(str(n))):
        res += count_of_twos_for_digit(n, i)
    return res


def count_of_twos_for_digit(x, d):
    power_of_ten = 10 ** d
    next_power_of_ten = power_of_ten * 10
    right = x % power_of_ten

    round_down = x - (x % next_power_of_ten)
    round_up = round_down + next_power_of_ten

    digit = int(x / power_of_ten) % 10
    if digit < 2:
        return round_down / 10
    elif digit == 2:
        return round_down / 10 + right + 1
    else:
        return round_up / 10


class Test(unittest.TestCase):
    def test_count_of_twos(self):
        self.assertEqual(1, count_of_twos(2))
        self.assertEqual(1, count_of_twos(10))
        self.assertEqual(2, count_of_twos(13))
        self.assertEqual(13, count_of_twos(30))
        self.assertEqual(20, count_of_twos(100))
        self.assertEqual(41, count_of_twos(200))
        self.assertEqual(160, count_of_twos(300))
        self.assertEqual(176, count_of_twos(355))
        self.assertEqual(300, count_of_twos(1000))
        self.assertEqual(4000, count_of_twos(10000))
        self.assertEqual(4000, count_of_twos(10000))
