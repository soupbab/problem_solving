class Stack:

    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return -1 if self.size() == 0 else self.data.pop()

    def size(self):
        return len(self.data)

    def empty(self):
        return 1 if len(self.data) == 0 else 0

    def top(self):
        return self.data[-1] if self.size() > 0 else -1
