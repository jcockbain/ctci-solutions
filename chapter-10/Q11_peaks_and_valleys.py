import unittest


def peaks_and_valleys(arr):
    for i in range(1, len(arr) - 1, 2):
        if arr[i + 1] > arr[i] > arr[i - 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        elif arr[i - 1] > arr[i] > arr[i + 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr


class Test(unittest.TestCase):
    def test_peaks_and_valleys(self):
        self.assertEqual([3, 5, 1, 3, 2], peaks_and_valleys([5, 3, 1, 2, 3]))
        self.assertEqual([0, 2, 1], peaks_and_valleys([0, 1, 2]))
        self.assertEqual([0, 2, 1, 4, 3, 5], peaks_and_valleys([0, 1, 2, 3, 4, 5]))
