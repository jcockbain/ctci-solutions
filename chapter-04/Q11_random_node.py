import unittest
import random


class RandomTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.nodes_below = 1

    def predecessor(self):
        node = self.left
        while node.right:
            node = node.right
        return node.val

    def successor(self):
        node = self.right
        while node.left:
            node = node.left
        return node.val

    def insert(self, val):
        self.nodes_below += 1
        if val < self.val:
            if not self.left:
                self.left = RandomTreeNode(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if not self.right:
                self.right = RandomTreeNode(val)
            else:
                self.right.insert(val)

    def delete(self, val):
        self.nodes_below -= 1

        if val > self.val:
            if not self.right:
                return
            self.right = self.right.delete(val)

        if val < self.val:
            if not self.left:
                return
            self.left = self.left.delete(val)

        else:
            if not (self.left or self.right):
                self = None

            elif self.right:
                successor = self.successor()
                self.val = successor
                self.right = self.right.delete(successor)

            else:
                predecessor = self.predecessor()
                self.val = predecessor
                self.left = self.left.delete(predecessor)

        return self

    def find(self, val):
        if self.val == val:
            return self
        if val > self.val:
            if not self.right:
                return
            return self.right.find(val)
        elif val < self.val:
            if not self.left:
                return
            return self.left.find(val)

    def get_random_node(self):
        if not self.left and not self.right:
            return self
        rand = random.randint(0, self.nodes_below)

        if rand == 0:
            return self

        if not self.right:
            return self.left.get_random_node()

        if not self.left:
            return self.right.get_random_node()

        if rand <= self.left.nodes_below:
            return self.left.get_random_node()

        return self.right.get_random_node()


class Test(unittest.TestCase):
    def test_random_node(self):
        root = RandomTreeNode(5)
        root.insert(10)
        root.insert(3)
        self.assertEqual(3, root.predecessor())

        root.insert(1)
        root.insert(4)
        self.assertEqual(4, root.predecessor())
        self.assertEqual(10, root.right.val)
        self.assertEqual(3, root.left.val)
        self.assertEqual(1, root.left.left.val)
        self.assertEqual(4, root.left.right.val)
        self.assertEqual(5, root.nodes_below)
        root.delete(3)

        self.assertEqual(4, root.nodes_below)
        self.assertEqual(4, root.left.val)
        self.assertEqual(1, root.left.left.val)
        root.insert(6)
        root.insert(12)
        root.insert(15)
        self.assertEqual(6, root.find(6).val)
        self.assertEqual(15, root.find(12).right.val)
        self.assertEqual(None, root.find(15).left)

        self.assertEqual(None, root.find(20))
        self.assertEqual(None, root.find(0))

        values = [10, 1, 4, 5, 6, 12, 15]
        for _ in range(10):
            node = root.get_random_node()
            self.assertEqual(True, node.val in values)

        for val in values:
            root.delete(val)

