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
    t = int(sys.stdin.readline().rstrip())

    for _ in range(t):
        box = Deque()
        r = 1
        p = sys.stdin.readline().rstrip()
        n = int(sys.stdin.readline().rstrip())
        numbers = sys.stdin.readline().rstrip()
        if numbers != "[]":
            numbers = list(map(int, numbers[1:-1].split(",")))

            for i in numbers:
                box.push_back(i)

        for j in p:
            if j == "R":
                r *= -1
            else:
                if box.size() == 0:
                    print("error")
                    break
                if r == 1:
                    box.pop_front()
                else:
                    box.pop_back()

        else:
            if r == 1:
                answer = "["
                for k in box.data:
                    answer = answer + str(k) + ","
                answer = answer[:-1] + "]"
            else:
                answer = "]"
                for k in box.data:
                    answer = "," + str(k) + answer
                answer = "[" + answer[1:]

            if len(answer) == 1:
                answer = "[]"

            print(answer)
