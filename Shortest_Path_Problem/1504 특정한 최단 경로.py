# import sys
#
# n, e = map(int, input().split())
#
# INF = int(1e9)
# table = [[INF] * (n + 1) for _ in range(n + 1)]
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             table[i][j] = 0
#
# for _ in range(e):
#     a, b, c = map(int, sys.stdin.readline().rstrip().split())
#     table[a][b] = c
#     table[b][a] = c
#
# for k in range(n + 1):
#     for i in range(n + 1):
#         for j in range(n + 1):
#             table[i][j] = min(table[i][j], table[i][k] + table[k][j])
#
# p1, p2 = map(int, input().split())
# distance = min(table[1][p1] + table[p1][p2] + table[p2][n], table[1][p2] + table[p2][p1] + table[p1][n])
#
# print(distance) if distance < INF else print(-1)

########################################################################################################################

import sys
import heapq

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (n + 1)
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

    return distance


p1, p2 = map(int, input().split())

start_ = dijkstra(1)
p1_ = dijkstra(p1)
p2_ = dijkstra(p2)

answer = min(start_[p1] + p1_[p2] + p2_[n], start_[p2] + p2_[p1] + p1_[n])
print(answer if answer < INF else -1)
