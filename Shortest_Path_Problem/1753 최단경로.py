import sys
import heapq

v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))

INF = int(1e9)
distance = [INF] * (v + 1)


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
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost


dijkstra(start)

for j in distance[1:]:
    print(j) if j < INF else print("INF")
