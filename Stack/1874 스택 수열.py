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
    n = int(sys.stdin.readline().rstrip())
    numbers = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    box = Stack()
    answer = []

    for i in range(1, n+1):
        box.push(i)
        answer.append("+")

        while box.top() == numbers[0]:
            box.pop()
            numbers.pop(0)
            answer.append("-")

            if len(numbers) == 0:
                break

    if box.size() > 0:
        print("NO")
    else:
        for i in answer:
            print(i)
