import unittest


def draw_line(screen, width, x1, x2, y):
    byte_width = width / 8
    height = len(screen) / byte_width

    byte = y * byte_width
    pass
    # while


class Test(unittest.TestCase):
    def test_draw_line(self):
        screen = [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ]
        draw_line(screen, 64, 20, 42, 1)

    # self.assertEqual(screen, [0] * 8 + [0, 0, 15, 255, 255, 192, 0, 0] + [0] * 8)

