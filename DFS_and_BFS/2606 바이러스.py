import sys


def dfs(v, data, visited):
    visited[v] = True

    for i in data[v]:
        if visited[i] is False:
            dfs(i, data, visited)

    return visited.count(True) - 1


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    v = 1
    data = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]

    for i in range(m):
        start, end = map(int, sys.stdin.readline().rstrip().split())
        data[start].append(end)
        data[end].append(start)

    for j in range(n+1):
        data[j].sort()

    print(dfs(v, data, visited))
