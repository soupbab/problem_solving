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


n, m = map(int, input().split())

parent = list(range(n + 1))

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == 0:
        union_parent(parent, b, c)
    else:
        print("YES" if find_parent(parent, b) == find_parent(parent, c) else "NO")
