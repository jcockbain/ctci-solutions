import unittest
from collections import defaultdict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def best_line(points):
    n = len(points)
    lines = defaultdict(int)
    for i in range(n):
        for j in range(i + 1, n):
            line_m, line_c = get_line(points[i], points[j])
            lines[(line_m, line_c)] += 1
    most_common_line = [line for line in lines if lines[line] == max(lines.values())][0]
    if most_common_line[0] == float("inf"):
        raise Exception(
            "Most common line is vertical line through x = {}".format(
                most_common_line[1]
            )
        )
    return lambda x: (most_common_line[0] * x) + most_common_line[1]


def get_line(point_a, point_b):
    m = get_gradient(point_a, point_b)
    # key by x intercept when vertical line
    if m == float("inf"):
        return m, point_a.x
    c = get_intersection(m, point_a)
    return (m, c)


def get_gradient(start, end):
    dy = end.y - start.y
    dx = end.x - start.x
    if dx == 0:
        return float("inf")
    return dy / dx


def get_intersection(gradient, point):
    c = point.y - (gradient * point.x)
    return c


class Test(unittest.TestCase):
    def test_best_lines(self):
        points = [
            Point(0, 0),
            Point(1, 1),
            Point(2, 2),
            Point(4, 4),
            Point(5, 6),
            Point(3, 1),
        ]
        best_line_fn = best_line(points)
        self.assertEqual(6, best_line_fn(6))
        self.assertEqual(8, best_line_fn(8))

    def test_best_lines_inf_gradient(self):
        points = [
            Point(0, 0),
            Point(0, 1),
            Point(0, 2),
            Point(4, 4),
            Point(0, 6),
            Point(3, 1),
        ]
        with self.assertRaises(Exception) as context:
            best_line_fn = best_line(points)
        self.assertTrue(
            "Most common line is vertical line through x = 0" in str(context.exception)
        )
