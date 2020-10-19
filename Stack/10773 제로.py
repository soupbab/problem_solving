import sys


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


if __name__ == "__main__":
    k = int(sys.stdin.readline().rstrip())
    box = Stack()

    for _ in range(k):
        number = int(sys.stdin.readline().rstrip())

        if number != 0:
            box.push(number)
        else:
            box.pop()

    print(sum(box.data))
