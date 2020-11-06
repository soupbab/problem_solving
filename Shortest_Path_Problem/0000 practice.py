# p.259 미래 도시 #######################################################################################################

n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j] = 1
    graph[j][i] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

x, k = map(int, input().split())
answer = graph[1][k] + graph[k][x]

print(answer) if answer < INF else print(-1)

# p.262 전보 ############################################################################################################

import sys
import heapq

n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append((y, z))

INF = int(1e9)
distance = [INF] * (n + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

count = 0
max_time = 0
for d in distance:
    if d != INF:
        count += 1
        max_time = max(max_time, d)

print(count - 1, max_time)

########################################################################################################################
