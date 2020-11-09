import sys
import heapq

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))

p1, p2 = map(int, input().split())
check = [[False] * 2 for _ in range(n + 1)]

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
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost

                if i[]

