import unittest


def get_max_height(boxes, w=float("inf"), d=float("inf"), h=float("inf")):
    boxes.sort(reverse=True, key=lambda x: x[0])
    dp = [None] * len(boxes)

    def helper(idx, w=float("inf"), d=float("inf"), h=float("inf")):
        if idx == len(boxes):
            return 0

        if not dp[idx]:
            box = boxes[idx]
            h1 = helper(idx + 1, w, d, h)
            h2 = float("inf")
            if box[0] < w and box[1] < d and box[2] < h:
                h2 = box[2] + helper(idx + 1, w + box[0], d + box[1], h + box[2])
            dp[idx] = max(h1, h2)
        return dp[idx]

    return helper(0)


class Test(unittest.TestCase):
    def test_get_max_height(self):
        boxes = [(1, 1, 2), (2, 2, 3), (3, 3, 2)]
        self.assertEqual(7, get_max_height(boxes))
        boxes = [(1, 1, 2), (2, 2, 3), (3, 2, 2)]
        self.assertEqual(7, get_max_height(boxes))
