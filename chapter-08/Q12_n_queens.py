import unittest


def ways_to_place_queens(n):
    cols = [0] * n
    diag_1 = [0] * ((2 * n) - 1)
    diag_2 = [0] * ((2 * n) - 1)
    positions = set()
    output = []

    def place_queen(row, col):
        diag_1_idx = (col - row) + (n - 1)
        diag_2_idx = col + row
        cols[col] = 1
        diag_1[diag_1_idx] = 1
        diag_2[diag_2_idx] = 1
        positions.add((row, col))

    def remove_queen(row, col):
        diag_1_idx = (col - row) + (n - 1)
        diag_2_idx = col + row
        cols[col] = 0
        diag_1[diag_1_idx] = 0
        diag_2[diag_2_idx] = 0
        positions.remove((row, col))

    def backtrack(row):
        for col in range(n):
            diag_1_idx = (col - row) + (n - 1)
            diag_2_idx = col + row
            if cols[col] == 0 and diag_1[diag_1_idx] == 0 and diag_2[diag_2_idx] == 0:
                place_queen(row, col)
                if row + 1 == n and sum(cols) == n:
                    add_output()
                else:
                    backtrack(row + 1)
                remove_queen(row, col)

    def add_output():
        res = []
        for row in range(n):
            res.append([])
            for col in range(n):
                if (row, col) in positions:
                    res[-1].append(1)
                else:
                    res[-1].append(0)
        output.append(res)

    backtrack(0)
    return output


class Test(unittest.TestCase):
    def test_ways_to_place_queens(self):
        four_solution = [
            [[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]],
            [[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]],
        ]
        self.assertEqual([], ways_to_place_queens(3))
        self.assertEqual(four_solution, ways_to_place_queens(4))
        self.assertEqual(four_solution, ways_to_place_queens(4))
        self.assertEqual(92, len(ways_to_place_queens(8)))
