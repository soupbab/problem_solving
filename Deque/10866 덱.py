import sys
from _collections import deque


class Deque:
    def __init__(self):
        self.data = deque([])

    def push_front(self, data):
        self.data.appendleft(data)

    def push_back(self, data):
        self.data.append(data)

    def pop_front(self):
        return self.data.popleft() if self.size() > 0 else -1

    def pop_back(self):
        return self.data.pop() if self.size() > 0 else -1

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
    box = Deque()

    for _ in range(n):
        command = sys.stdin.readline().rstrip()

        if "push_front" in command:
            box.push_front(int(command.split()[1]))

        elif "push_back" in command:
            box.push_back(int(command.split()[1]))

        elif command == "pop_front":
            print(box.pop_front())

        elif command == "pop_back":
            print(box.pop_back())

        elif command == "size":
            print(box.size())

        elif command == "empty":
            print(box.empty())

        elif command == "front":
            print(box.front())

        elif command == "back":
            print(box.back())
