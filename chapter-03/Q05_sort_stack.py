import unittest


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.stack:
            return
        return self.stack[-1]


def sort_stack(stack):
    sorted_stack = Stack()
    temp = None

    while not stack.is_empty():
        temp = stack.pop()
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            stack.push(sorted_stack.pop())
        sorted_stack.push(temp)

    return sorted_stack


class SetOfStacksTest(unittest.TestCase):
    def test_sort_stack(self):
        stack = Stack()
        self.assertEqual(None, stack.peek())
        stack.push(2)
        stack.push(3)
        stack.push(1)
        stack.push(4)

        sorted_stack = sort_stack(stack)

        self.assertEqual(4, sorted_stack.pop())
        self.assertEqual(3, sorted_stack.pop())
        self.assertEqual(2, sorted_stack.pop())
        self.assertEqual(1, sorted_stack.pop())
