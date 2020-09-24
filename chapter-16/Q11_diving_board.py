import unittest


def diving_board(shorter, longer, k):
    lengths = []
    for i in range(k + 1):
        lengths.append(i * longer + (k - i) * shorter)

    return lengths


class Test(unittest.TestCase):
    def test_diving_board(self):
        shorter = 1
        longer = 2
        k = 4
        self.assertEqual([4, 5, 6, 7, 8], diving_board(shorter, longer, k))

        shorter = 1
        longer = 3
        k = 1
        self.assertEqual([1, 3], diving_board(shorter, longer, k))

        shorter = 1
        longer = 3
        k = 3
        self.assertEqual([3, 5, 7, 9], diving_board(shorter, longer, k))
