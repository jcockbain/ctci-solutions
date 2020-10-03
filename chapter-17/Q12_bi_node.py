import unittest


class BiNode:
    def __init__(self, val, node_1=None, node_2=None):
        self.val = val
        self.node_1 = node_1
        self.node_2 = node_2


def convert_bst_to_ll(root):
    if root is None:
        return None, None

    start_left_ll, end_left_ll = convert_bst_to_ll(root.node_1)
    start_right_ll, end_right_ll = convert_bst_to_ll(root.node_2)

    if end_left_ll:
        root.node_1 = end_left_ll
        root.node_1.node_2 = root

    if start_right_ll:
        root.node_2 = start_right_ll
        root.node_2.node_1 = root

    return (
        root if not start_left_ll else start_left_ll,
        root if not end_right_ll else end_right_ll,
    )


class Test(unittest.TestCase):
    def test_convert_bst_to_ll(self):
        bst = BiNode(
            10, BiNode(5, BiNode(2), BiNode(7)), BiNode(15, BiNode(12), BiNode(18))
        )
        head = convert_bst_to_ll(bst)[0]
        self.assertEqual(None, head.node_1)
        self.assertEqual(2, head.val)
        self.assertEqual(5, head.node_2.val)
        self.assertEqual(7, head.node_2.node_2.val)
        self.assertEqual(10, head.node_2.node_2.node_2.val)
        self.assertEqual(12, head.node_2.node_2.node_2.node_2.val)
        self.assertEqual(15, head.node_2.node_2.node_2.node_2.node_2.val)
        self.assertEqual(18, head.node_2.node_2.node_2.node_2.node_2.node_2.val)
