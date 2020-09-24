import unittest

# TODO: Handle no intersection


def intersection(line_1, line_2):
    line_1_m = get_gradient(line_1[0], line_1[1])
    line_1_c = get_intersection(line_1_m, line_1[0])

    line_2_m = get_gradient(line_2[0], line_2[1])
    line_2_c = get_intersection(line_2_m, line_2[0])

    if line_1_m == line_2_m:
        raise Exception("Lines with the same gradient are invalid")

    x_intersection = (line_2_c - line_1_c) / (line_1_m - line_2_m)
    y_intersection = (line_1_m * x_intersection) + line_1_c

    # if x_intersection < min(line_1[0][0], line_1[1][0]) or x_intersection > min(
    #     line_2[0][0], line_2[1][0]
    # ):
    #     raise Exception("No intersection")

    return (x_intersection, y_intersection)


def get_gradient(start, end):
    dy = end[1] - start[1]
    dx = end[0] - start[0]
    return dy / dx


def get_intersection(gradient, point):
    c = point[1] - (gradient * point[0])
    return c


class Test(unittest.TestCase):
    def test_intersection(self):
        line_1 = [(1, 3), (5, 7)]
        line_2 = [(1, 5), (3, 3)]
        self.assertEqual((2, 4), intersection(line_1, line_2))

        with self.assertRaises(Exception) as context:
            res = intersection([(1, 1), (3, 3)], [(0, 0), (2, 2)])
        self.assertTrue(
            "Lines with the same gradient are invalid" in str(context.exception)
        )

        # with self.assertRaises(Exception) as context:
        #     res = intersection([(3, 5), (5, 7)], [(0, 0), (2, 2)])
        # self.assertTrue("No intersection" in str(context.exception))

