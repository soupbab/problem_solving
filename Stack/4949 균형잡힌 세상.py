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
    while True:
        data = sys.stdin.readline().rstrip()

        if data == ".":
            break

        box = Stack()
        brackets = {")": "(", "}": "{", "]": "["}

        for i in data:
            if i in brackets.values():
                box.push(i)
            elif i in brackets:
                if box.top() == brackets[i]:
                    box.pop()
                else:
                    print("no")
                    break
            else:
                continue
        else:
            if box.size() == 0:
                print("yes")
            else:
                print("no")
