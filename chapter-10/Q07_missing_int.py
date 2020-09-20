import unittest


# TODO: Follow-up


def missing_int(ints):
    max_n = 1 << 32
    bit_array = BitArray(max_n)
    for n in ints:
        bit_array.set(n)

    for n in range(max_n):
        if not bit_array.get(n):
            return n


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
        self.assertEqual(7, missing_int([0, 1, 2, 3, 4, 5, 6, 8, 9, 10]))
        self.assertEqual(2, missing_int([0, 1, 3, 4, 5, 6, 8, 9, 10]))
