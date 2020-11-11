import sys

n = int(input())
m = int(input())

INF = int(1e9)
table = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            table[i][j] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    table[a][b] = min(table[a][b], c)

for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            table[i][j] = min(table[i][j], table[i][k] + table[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(table[i][j] if table[i][j] < INF else 0, end=" ")
    print()
