import sys

if __name__ == "__main__":
    n = int(input())
    numbers = []

    for _ in range(n):
        numbers.append(int(sys.stdin.readline().rstrip()))

    numbers.sort()

    for i in numbers:
        print(i)
