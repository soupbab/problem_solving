# p.298 팀 결성 #########################################################################################################

import sys


def check_team(array, x):
    if array[x] != x:
        array[x] = check_team(team, array[x])

    return array[x]


def join_team(array, x, y):
    x = check_team(array, x)
    y = check_team(array, y)

    if x < y:
        array[y] = x
    else:
        array[x] = y


n, m = map(int, input().split())

team = [0] * (n + 1)
for i in range(n + 1):
    team[i] = i

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == 1:
        print("YES" if check_team(team, b) == check_team(team, c) else "NO")
    else:
        join_team(team, b, c)

# p.300 도시 분할 계획 ###################################################################################################

import sys


def find_city(array, x):
    if array[x] != x:
        array[x] = find_city(array, array[x])

    return array[x]


def join_city(array, x, y):
    x = find_city(array, x)
    y = find_city(array, y)

    if x < y:
        array[y] = x
    else:
        array[x] = y


n, m = map(int, input().split())

city = [0] * (n + 1)
for i in range(1, n + 1):
    city[i] = i

cost = 0
cost_sum = 0

routes = []
for i in range(m):
    routes.append(list(map(int, sys.stdin.readline().rstrip().split())))

routes.sort(key=lambda x: x[2])

for route in routes:
    if find_city(city, route[0]) != find_city(city, route[1]):
        join_city(city, route[0], route[1])
        cost = route[2]
        cost_sum += cost

cost_sum -= cost

print(cost_sum)

# p.303 커리큘럼 ########################################################################################################

import sys
from collections import deque
from copy import deepcopy

n = int(input())

time = [0] * (n + 1)
indegree = [0] * (n + 1)
table = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    values = list(map(int, sys.stdin.readline().rstrip().split()))[:-1]
    time[i] = values[0]

    for preceding_subject in values[1:]:
        indegree[i] += 1
        table[preceding_subject].append(i)


def topology_sort():
    q = deque()
    answer = deepcopy(time)

    for i in range(n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for trailing_subject in table[now]:
            answer[trailing_subject] = max(answer[trailing_subject], answer[now] + time[trailing_subject])
            indegree[trailing_subject] -= 1

        if indegree[trailing_subject] == 0:
            q.append(trailing_subject)

    for i in range(1, n + 1):
        print(answer[i])


topology_sort()

########################################################################################################################
