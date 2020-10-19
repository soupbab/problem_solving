import sys


def stack(stack, command):
    if "push" in command:
        splitted = command.split()
        data = int(splitted[1])
        stack.append(data)

    elif command == "pop":
        if len(stack) > 0:
            popped = stack.pop()
            print(popped)
        else:
            print(-1)

    elif command == "size":
        print(len(stack))

    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())

    box = []

    for _ in range(n):
        command = sys.stdin.readline().rstrip()

        stack(box, command)
