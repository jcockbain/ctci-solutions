import unittest


def check_duplicates(arr):
    bit_array = BitArray(32000)
    res = []
    for num in arr:
        if bit_array.get(num):
            res.append(num)
        bit_array.set(num)
    return res


class BitArray:
    def __init__(self, n):
        self.arr = [0] * ((n >> 5) + 1)

    def get(self, pos):
        index = pos >> 5
        bitNo = pos & 0x1F
        return (self.arr[index] & (1 << bitNo)) != 0

    def set(self, pos):
        index = pos >> 5
        bitNo = pos & 0x1F
        self.arr[index] |= 1 << bitNo


class Test(unittest.TestCase):
    def test_missing_int(self):
        self.assertEqual(
            [2, 3], check_duplicates([0, 1, 2, 2, 3, 4, 5, 6, 8, 9, 10, 12, 3])
        )
        self.assertEqual([], check_duplicates([0, 1, 3, 4, 5, 6, 8, 9, 10]))
