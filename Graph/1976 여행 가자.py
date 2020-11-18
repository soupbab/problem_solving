import sys


def find_parent(array, x):
    if array[x] != x:
        array[x] = find_parent(array, array[x])

    return array[x]


def union_parent(array, x, y):
    x = find_parent(array, x)
    y = find_parent(array, y)

    if x < y:
        array[y] = x
    else:
        array[x] = y


n = int(input())
m = int(input())

parent = list(range(n + 1))

for i in range(1, n + 1):
    route = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

    for j in range(1, len(route)):
        if route[j] == 1:
            union_parent(parent, i, j)

plan = list(map(int, input().split()))

for i in range(1, m):
    if find_parent(parent, plan[0]) != find_parent(parent, plan[i]):
        print("NO")
        break
else:
    print("YES")
