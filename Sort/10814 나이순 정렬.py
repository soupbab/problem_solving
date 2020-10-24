import sys

if __name__ == "__main__":
    n = int(input())
    info = []

    for i in range(n):
        age, name = sys.stdin.readline().rstrip().split()
        info.append((int(age), name, i))

    info.sort(key=lambda t: t[2])
    info.sort(key=lambda t: t[0])

    for i in info:
        print(i[0], i[1])
