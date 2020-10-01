import unittest
from enum import Enum, IntEnum
from collections import defaultdict

WHITE = 0
BLACK = 1


class Grid:
    def __init__(self):
        self.squares = defaultdict(int)
        self.min_x, self.max_x = -1, 1
        self.min_y, self.max_y = -1, 1

    def at(self, x, y):
        return self.squares[(x, y)]

    def flip(self, x, y):
        self.squares[(x, y)] ^= BLACK
        self.min_x = min(self.min_x, x - 1)
        self.max_x = max(self.max_x, x + 1)
        self.min_y = min(self.min_y, y - 1)
        self.max_y = max(self.max_y, y + 1)

    def __str__(self):
        num_cols = 2 * (self.max_x - self.min_x) + 3
        res = ["\n+" + "-" * num_cols + "+\n"]
        for row in range(self.min_y, self.max_y + 1):
            res.append("| ")
            for col in range(self.min_x, self.max_x + 1):
                if self.at(col, row) == WHITE:
                    res.append("□ ")
                else:
                    res.append("■ ")
            res.append("|\n")
        res.append("+" + "-" * num_cols + "+\n")
        return "".join(res)


def langtons_ant(k):
    grid = Grid()

    direction = (1, 0)
    x, y = 0, 0

    for _ in range(k):
        direction = (
            (-direction[1], direction[0])
            if grid.at(x, y) == WHITE
            else (direction[1], -direction[0])
        )
        grid.flip(x, y)
        x, y = (x + direction[0], y + direction[1])

    return str(grid)


class Test(unittest.TestCase):
    def test_langtons_ant(self):
        expected = """
+-----------+
| □ □ □ □ □ |
| □ ■ ■ □ □ |
| □ □ ■ ■ □ |
| □ ■ ■ ■ □ |
| □ ■ ■ □ □ |
| □ □ □ □ □ |
+-----------+
"""
        self.assertEqual(expected, langtons_ant(15))

        expected = """
+-----------------+
| □ □ □ □ □ □ □ □ |
| □ □ □ ■ ■ □ □ □ |
| □ □ ■ □ □ ■ □ □ |
| □ ■ □ □ □ □ ■ □ |
| □ ■ □ ■ □ □ ■ □ |
| □ □ ■ □ ■ ■ □ □ |
| □ □ □ □ □ □ □ □ |
+-----------------+
"""
        self.assertEqual(expected, langtons_ant(50))

        expected = """
+-----------------------+
| □ □ □ □ □ □ □ □ □ □ □ |
| □ □ □ ■ ■ □ □ □ □ □ □ |
| □ □ ■ □ □ ■ □ □ □ □ □ |
| □ ■ □ □ □ ■ ■ □ ■ □ □ |
| □ ■ □ ■ ■ ■ □ ■ □ ■ □ |
| □ □ ■ □ □ □ □ □ □ ■ □ |
| □ □ □ □ □ ■ □ □ ■ □ □ |
| □ □ □ □ □ □ ■ ■ □ □ □ |
| □ □ □ □ □ □ □ □ □ □ □ |
+-----------------------+
"""
        self.assertEqual(expected, langtons_ant(100))

