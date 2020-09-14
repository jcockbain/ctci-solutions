import unittest


class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, num):
        if self.stacks == [] or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(num)

    def pop(self):
        if self.stacks == []:
            raise ValueError("Cannot pop from empty stack")

        if self.stacks[-1] == []:
            self.stacks.pop()

        if self.stacks == []:
            raise ValueError("Cannot pop from empty stack")

        return self.stacks[-1].pop()


class SetOfStacksTest(unittest.TestCase):
    def test_set_of_stacks(self):
        stack = SetOfStacks(2)
        self.assertRaises(ValueError, stack.pop)
        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.pop())
        stack.push(3)
        stack.push(4)
        self.assertEqual(4, stack.pop())
        stack.pop()
        self.assertEqual(1, stack.pop())
        self.assertRaises(ValueError, stack.pop)
