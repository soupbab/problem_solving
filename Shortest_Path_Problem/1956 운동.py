import sys

v, e = map(int, input().split())

INF = int(1e9)
table = [[INF] * (v + 1) for _ in range(v + 1)]
for i in range(v + 1):
    for j in range(v + 1):
        if i == j:
            table[i][j] = 0

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    table[a][b] = c

for k in range(v + 1):
    for i in range(v + 1):
        for j in range(v + 1):
            table[i][j] = min(table[i][j], table[i][k] + table[k][j])

plans = []
for i in range(v + 1):
    for j in range(v + 1):
        if i != j:
            plans.append(table[i][j] + table[j][i])

print(min(plans) if min(plans) < INF else -1)
