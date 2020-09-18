import unittest


def rotate_matrix(m):
    n = len(m)
    res = [[0] * n] * n
    for y in range(n):
        for x in range(n):
            res[y][x] = m[x][y]
        res[y] = res[y][::-1]
    return res


class Test(unittest.TestCase):
    def test_rotate_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ]
        self.assertEqual(expected, rotate_matrix(matrix))
