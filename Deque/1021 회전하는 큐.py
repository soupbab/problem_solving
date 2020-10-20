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
    n, m = map(int, input().split())
    box = Deque()
    goal = list(map(int, input().split()))
    count = 0
    i = 0

    for j in range(1, n+1):
        box.push_back(j)

    while i < len(goal):
        if goal[i] == box.data[0]:
            box.pop_front()
            i += 1
        else:
            if box.data.index(goal[i]) < box.size() / 2:
                box.push_back(box.pop_front())
                count += 1
            else:
                box.push_front(box.pop_back())
                count += 1

    print(count)
