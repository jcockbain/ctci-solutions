import unittest
import random


def rand_5():
    return random.randint(0, 4)


def rand_7(rand_5):
    conversion = [
        [0, 1, 2, 3, 4],
        [5, 6, 0, 1, 2],
        [3, 4, 5, 6, 0],
        [1, 2, 3, 4, 5],
        [6, -1, -1, -1, -1],
    ]
    a, b = rand_5(), rand_5()
    if conversion[b][a] == -1:
        return rand_7(rand_5)
    return conversion[b][a]


class Test(unittest.TestCase):
    def test_rand_7(self):
        self.assertEqual(0, rand_7(lambda: 0))
        self.assertEqual(6, rand_7(lambda: 1))
        self.assertEqual(5, rand_7(lambda: 2))
        self.assertEqual(4, rand_7(lambda: 3))
