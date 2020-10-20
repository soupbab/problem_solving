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

    for _ in range(n):
        command = sys.stdin.readline().rstrip()

        if "push" in command:
            box.push(int(command.split()[1]))

        elif command == "pop":
            print(box.pop())

        elif command == "size":
            print(box.size())

        elif command == "empty":
            print(box.empty())

        elif command == "front":
            print(box.front())

        elif command == "back":
            print(box.back())
