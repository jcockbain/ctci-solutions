import unittest


class Square:
    def __init__(self, center, side):
        self.center = center
        self.side = side


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_gradient(start, end):
    dy = end.y - start.y
    dx = end.x - start.x
    if dx == 0:
        return float("inf")
    return dy / dx


def get_intersection(gradient, point):
    c = point.y - (gradient * point.x)
    return c


def bisect_squares(square_1, square_2):
    m = get_gradient(square_1.center, square_2.center)
    if m == float("inf"):
        raise ValueError("Line bisecting is vertical")
    c = get_intersection(m, square_1.center)
    return lambda x: (m * x) + c


class Test(unittest.TestCase):
    def test_bisect_squares(self):
        square_1 = Square(Point(0.5, 0.5), 1)
        square_2 = Square(Point(-0.5, -0.5), 1)
        res = bisect_squares(square_1, square_2)
        self.assertEqual(1, res(1))
        self.assertEqual(0, res(0))

        square_1 = Square(Point(0.5, 0.5), 1)
        square_2 = Square(Point(2.5, 0.5), 1)
        res = bisect_squares(square_1, square_2)
        self.assertEqual(0.5, res(10))
        self.assertEqual(0.5, res(-5))

        square_1 = Square(Point(0.5, 0.5), 1)
        square_2 = Square(Point(0.5, 2.5), 1)
        with self.assertRaises(Exception) as context:
            res = bisect_squares(square_1, square_2)
        self.assertTrue("Line bisecting is vertical" in str(context.exception))
