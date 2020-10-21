import sys


def dfs(x, y, data, visited, number):
    data[x][y] = number
    visited[x][y] = True
    neighbors = []

    if x > 0:
        neighbors.append((x - 1, y))
    if x < n - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < n - 1:
        neighbors.append((x, y + 1))

    for neighbor in neighbors:
        if data[neighbor[0]][neighbor[1]] == 1 and visited[neighbor[0]][neighbor[1]] is False:
            dfs(neighbor[0], neighbor[1], data, visited, number)


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    data = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    group = []
    number = 0

    for i in range(n):
        for j in range(n):
            if data[i][j] == 1 and visited[i][j] is False:
                number += 1
                dfs(i, j, data, visited, number)

    for k in range(1, number+1):
        count = 0

        for i in range(n):
            for j in range(n):
                if data[i][j] == k:
                    count += 1

        group.append(count)

    print(len(group))
    for k in sorted(group):
        print(k)
