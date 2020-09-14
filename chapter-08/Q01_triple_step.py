import unittest


def triple_hop(x):
    if x < 0:
        return 0
    if x == 0:
        return 1
    if x == 1:
        return 1
    return triple_hop(x - 1) + triple_hop(x - 2) + triple_hop(x - 3)


def Method2(x):
    memo = [-1] * (x + 1)
    return triple_hop_recursive(x, memo)


def triple_hop_recursive(x, memo):
    if x < 0:
        return 0
    memo[0] = 1
    if x >= 1:
        memo[1] = 1
    if x >= 2:
        memo[2] = memo[1] + memo[0]
    if x > 2:
        for i in range(3, x + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[x]


def triple_step(n):
    counts = [1, 1, 2]
    if n < 3:
        return counts[n]
    i = 2
    while i < n:
        i += 1
        counts[i % 3] = sum(counts)
    return counts[i % 3]


class Test(unittest.TestCase):
    def test_triple_step(self):
        self.assertEqual(Method2(3), 4)
        self.assertEqual(Method2(7), 44)


if __name__ == "__main__":
    unittest.main()
