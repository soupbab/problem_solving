import sys
from _collections import deque


class Queue:
    def __init__(self):
        self.data = deque([])

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.popleft() if self.size() > 0 else -1

    def size(self):
        return len(self.data)

    def empty(self):
        return 1 if self.size() == 0 else 0

    def front(self):
        return self.data[0] if self.size() > 0 else -1

    def back(self):
        return self.data[-1] if self.size() > 0 else -1


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    box = Queue()

    for i in range(1, n+1):
        box.push(i)

    while box.size() > 1:
        box.pop()
        box.push(box.pop())

    print(box.front())
