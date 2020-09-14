import unittest


class StackQueue:
    def __init__(self):
        self.new_stack = []
        self.old_stack = []

    def dequeue(self):
        self.stack_shift()
        return self.old_stack.pop()

    def enqueue(self, x):
        self.new_stack.append(x)

    def stack_shift(self):
        if not self.old_stack:
            while self.new_stack:
                self.old_stack.append(self.new_stack.pop())


class Test(unittest.TestCase):
    def test_stack_queue(self):
        queue = StackQueue()
        queue.enqueue(1)
        res = queue.dequeue()
        self.assertEqual(1, res)

        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)

        self.assertEqual(2, queue.dequeue())
        self.assertEqual(3, queue.dequeue())
