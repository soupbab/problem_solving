import sys
import heapq
INF = int(1e9)


def dijkstra(start, point):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (point + 1)
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

    return distance


T = int(input())

for test_case in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    start_ = dijkstra(s, n)
    g_ = dijkstra(g, n)
    h_ = dijkstra(h, n)

    candidate = []
    for _ in range(t):
        goal = int(sys.stdin.readline().rstrip())
        dist_2 = min(start_[g] + g_[h] + h_[goal], start_[h] + h_[g] + g_[goal])

        if dist_2 == start_[goal]:
            candidate.append(goal)

    candidate.sort()

    for j in candidate:
        print(j, end=" ")
    print()
