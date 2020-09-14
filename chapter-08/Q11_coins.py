import unittest


def change_possibilities(amount, denominations):
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1

    for coin in denominations:
        for curr_amount in range(coin, amount + 1):
            dp[curr_amount] += dp[curr_amount - coin]

    return dp[-1]


class CoinsTest(unittest.TestCase):
    def test_coin_test(self):
        actual = change_possibilities(50, [5, 10])
        expected = 6
        self.assertEqual(expected, actual)
