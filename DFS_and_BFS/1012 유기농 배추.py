import sys


def dfs(y, x, data):
    data[y][x] = 2
    neighbors = []

    if y > 0:
        neighbors.append((y - 1, x))
    if y < n - 1:
        neighbors.append((y + 1, x))
    if x > 0:
        neighbors.append((y, x - 1))
    if x < m - 1:
        neighbors.append((y, x + 1))

    for neighbor in neighbors:
        if data[neighbor[0]][neighbor[1]] == 1:
            dfs(neighbor[0], neighbor[1], data)


if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    answer = []

    for i in range(t):
        m, n, k = map(int, sys.stdin.readline().rstrip().split())
        data = [[0 for _ in range(m)] for _ in range(n)]
        count = 0

        for j in range(k):
            x, y = map(int, sys.stdin.readline().rstrip().split())
            data[y][x] = 1

        for o in range(n):
            for p in range(m):
                if data[o][p] == 1:
                    count += 1
                    dfs(o, p, data)

        answer.append(count)

    for num in answer:
        print(num)
