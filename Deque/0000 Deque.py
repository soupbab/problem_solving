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
