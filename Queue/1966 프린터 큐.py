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
    t = int(sys.stdin.readline().rstrip())

    for _ in range(t):
        n, m = map(int, sys.stdin.readline().rstrip().split())
        importance = list(map(int, sys.stdin.readline().rstrip().split()))
        print_queue = Queue()
        count = 0
        index = -1

        for idx, i in enumerate(importance):
            print_queue.push((idx, i))

        while index != m:
            largest = max(print_queue.data, key=lambda x: x[1])[1]

            if print_queue.front()[1] == largest:
                index = print_queue.pop()[0]
                count += 1
            else:
                print_queue.push(print_queue.pop())

        print(count)
