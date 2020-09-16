import unittest


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        if val <= self.peek_min():
            self.min_stack.append(val)
        self.stack.append(val)

    def peek(self):
        return self.stack[-1]

    def peek_min(self):
        if not self.min_stack:
            return float("inf")
        return self.min_stack[-1]

    def pop(self):
        value = self.stack.pop()
        if value == self.peek_min():
            self.min_stack.pop()
        return value


class Test(unittest.TestCase):
    def test_min_stack(self):
        min_stack = MinStack()
        min_stack.push(2)
        self.assertEqual(2, min_stack.peek())
        self.assertEqual(2, min_stack.peek_min())
        min_stack.push(1)
        self.assertEqual(1, min_stack.peek_min())
        self.assertEqual(1, min_stack.pop())
        self.assertEqual(2, min_stack.peek_min())

