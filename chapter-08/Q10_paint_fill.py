import unittest


def paint_fill_with_color(image, x, y, color):
    if x < 0 or x >= len(image[0]) or y < 0 or y >= len(image):
        return image
    old_color = image[y][x]
    paint_fill(image, x, y, color, old_color)


def paint_fill(image, x, y, color, old_color):
    neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if (
        x < 0
        or x >= len(image[0])
        or y < 0
        or y >= len(image)
        or image[y][x] != old_color
    ):
        return
    image[y][x] = color
    for neighbour in neighbours:
        paint_fill(image, x + neighbour[0], y + neighbour[1], color, old_color)


class Test(unittest.TestCase):
    def test_paint_fill(self):
        image1 = [
            [10, 10, 10, 10],
            [30, 20, 20, 10],
            [10, 10, 20, 20],
            [10, 10, 30, 20],
        ]
        image2 = [
            [10, 10, 10, 10],
            [30, 20, 20, 10],
            [30, 30, 20, 20],
            [30, 30, 30, 20],
        ]
        image3 = [
            [10, 10, 10, 10],
            [10, 20, 20, 10],
            [10, 10, 20, 20],
            [10, 10, 10, 20],
        ]
        paint_fill_with_color(image1, 0, 2, 30)
        self.assertEqual(image1, image2)
        paint_fill_with_color(image1, 0, 3, 10)
        self.assertEqual(image1, image3)
        paint_fill_with_color(image1, 5, 0, 50)
        self.assertEqual(image1, image3)

