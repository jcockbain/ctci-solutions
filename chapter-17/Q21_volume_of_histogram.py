import unittest


def volume_of_histogram(arr):
    total_water = 0
    current_max = 0
    forwards_peak = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        forwards_peak[i] = current_max
        current_max = max(current_max, arr[i])

    backwards_peak = 0
    for i in range(len(arr)):
        height = arr[i]
        forward_peak = forwards_peak[i]
        if backwards_peak > height and forwards_peak[i] > height:
            total_water += min(backwards_peak, forward_peak) - height
        backwards_peak = max(height, backwards_peak)

    return total_water


class Test(unittest.TestCase):
    def test_volume_of_histogram(self):
        bars = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0]
        self.assertEqual(26, volume_of_histogram(bars))

        bars = [0, 2, 4, 8]
        self.assertEqual(0, volume_of_histogram(bars))

        bars = [12, 0, 0, 12]
        self.assertEqual(24, volume_of_histogram(bars))

        bars = [12, 0, 0, 12, 6, 8, 10, 12]
        self.assertEqual(36, volume_of_histogram(bars))
