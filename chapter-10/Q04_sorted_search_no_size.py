import unittest


class Listy:
    def __init__(self, items):
        self.items = items

    def elementAt(self, i):
        try:
            return self.items[i]
        except IndexError:
            return -1


def sorted_search_no_size(listy, x):
    lower = 0
    upper = 1
    while listy.elementAt(upper) != -1:
        upper <<= 1

    while lower <= upper:
        mid = lower + ((upper - lower) // 2)
        elem = listy.elementAt(mid)
        if elem == x:
            return mid
        elif elem == -1 or elem > x:
            upper = mid - 1
        else:
            lower = mid + 1

    return -1


class Test(unittest.TestCase):
    def test_sorted_search_no_size(self):
        listy = Listy([1, 2, 3, 4, 5])
        self.assertEqual(2, sorted_search_no_size(listy, 3))
        listy = Listy([1, 2, 3, 4, 5, 7, 8, 9, 12])
        self.assertEqual(5, sorted_search_no_size(listy, 7))
        listy = Listy([1, 2, 3, 4, 5, 7, 8, 9, 12])
        self.assertEqual(-1, sorted_search_no_size(listy, 14))
