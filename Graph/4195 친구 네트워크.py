# import sys
#
#
# def find_parent(p_dict, x):
#     if p_dict[x] != x:
#         p_dict[x] = find_parent(p_dict, p_dict[x])
#
#     return p_dict[x]
#
# 
# def union_parent(p_dict, array, x, y):
#     x = find_parent(p_dict, x)
#     y = find_parent(p_dict, y)
#
#     if array.index(x) < array.index(y):
#         p_dict[y] = x
#     else:
#         p_dict[x] = y
#
#
# t = int(input())
# for _ in range(t):
#     parent = {}
#     order = []
#
#     f = int(input())
#     for _ in range(f):
#         a, b = sys.stdin.readline().rstrip().split()
#
#         if a not in parent:
#             parent[a] = a
#             order.append(a)
#
#         if b not in parent:
#             parent[b] = b
#             order.append(b)
#
#         order.sort()
#         union_parent(parent, order, a, b)
#
#         for i in parent.keys():
#             find_parent(parent, i)
#
#         c = min(order.index(parent[a]), order.index(parent[b]))
#         count = 0
#         for i in parent.values():
#             if i == order[c]:
#                 count += 1
#
#         print(count)

########################################################################################################################

import sys


def find_parent(p_dict, x):
    if p_dict[x] != x:
        p_dict[x] = find_parent(p_dict, p_dict[x])

    return p_dict[x]


def union_parent(p_dict, x, y):
    x = find_parent(p_dict, x)
    y = find_parent(p_dict, y)

    if x != y:
        parent[y] = x
        count[x] += count[y]


t = int(input())
for _ in range(t):
    parent = {}
    count = {}

    f = int(input())
    for _ in range(f):
        a, b = sys.stdin.readline().rstrip().split()

        if a not in parent:
            parent[a] = a
            count[a] = 1

        if b not in parent:
            parent[b] = b
            count[b] = 1

        union_parent(parent, a, b)

        print(count[find_parent(parent, a)])
