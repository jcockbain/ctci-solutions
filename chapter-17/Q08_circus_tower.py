import unittest


def circus_row(people):
    people.sort(key=lambda x: x[0])
    return get_longest_increading_subsequence([w for h, w in people])


def get_longest_increading_subsequence(weights):
    n = len(weights)
    dp = [0] * n
    dp[0] = 1

    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if weights[i] > weights[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


class Test(unittest.TestCase):
    def test_circus_row(self):
        people = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
        self.assertEqual(6, circus_row(people))

        people = [(5, 12), (8, 2), (6, 15), (9, 18), (11, 21), (7, 22)]
        self.assertEqual(4, circus_row(people))

