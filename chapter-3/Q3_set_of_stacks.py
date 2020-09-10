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

