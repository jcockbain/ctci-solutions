import unittest


def draw_line(screen, width, x1, x2, y):
    byte_width = int(width / 8)
    height = len(screen) / byte_width

    bits_to_draw = x2 - x1
    current_byte = y * byte_width + int(x1 // 8)
    starting_bit = x1 % 8
    mask = 1 << (7 - starting_bit)

    while bits_to_draw:
        if mask == 0:
            mask = 1 << 7
            current_byte += 1
        screen[current_byte] |= mask
        mask >>= 1
        bits_to_draw -= 1


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
        draw_line(screen, 64, 8, 16, 0)
        draw_line(screen, 64, 4, 30, 1)
        draw_line(screen, 64, 0, 64, 2)
        self.assertEqual(
            [0, 255, 0, 0, 0, 0, 0, 0] + [15, 255, 255, 252, 0, 0, 0, 0] + [255] * 8,
            screen,
        )

