import sys

if __name__ == "__main__":
    n = int(input())
    location = []

    for _ in range(n):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        location.append((x, y))

    location.sort(key=lambda t: t[1])
    location.sort(key=lambda t: t[0])

    for i in location:
        print(i[0], i[1])
