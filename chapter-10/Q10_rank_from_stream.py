import unittest


class RankNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        if self.val:
            self.count = 1
        else:
            self.count = 0
        self.left_count = 0

    def track(self, x):
        if not self.val:
            self.val = x
            self.count += 1

        elif self.val == x:
            self.count += 1

        elif self.val > x:
            if self.left:
                self.left.track(x)
            else:
                self.left = RankNode(x)
            self.left_count += 1

        else:
            if self.right:
                self.right.track(x)
            else:
                self.right = RankNode(x)

    def get_rank(self, x):
        if not self.val:
            return 0
        elif self.val < x:
            if self.right:
                return self.count + self.left_count + self.right.get_rank(x)
            else:
                return self.count + self.left_count
        elif self.val > x:
            if self.left:
                return self.left.get_rank(x)
            else:
                return 0
        else:
            return self.count + self.left_count


class Test(unittest.TestCase):
    def test_rank_from_stream(self):
        stream_rank = RankNode()
        stream_rank.track(1)
        stream_rank.track(2)
        stream_rank.track(2)
        stream_rank.track(3)
        stream_rank.track(4)
        self.assertEqual(3, stream_rank.get_rank(2))
        self.assertEqual(1, stream_rank.get_rank(1))
