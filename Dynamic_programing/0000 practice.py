# p.217 1로 만들기 ######################################################################################################

from collections import deque

x = int(input())
memo = [0] * (x + 1)
queue = deque([x])

while queue:
    popped = queue.popleft()

    if popped % 5 == 0:
        if memo[int(popped / 5)] == 0:
            memo[int(popped / 5)] = memo[popped] + 1
            queue.append(int(popped / 5))

    if popped % 3 == 0:
        if memo[int(popped / 3)] == 0:
            memo[int(popped / 3)] = memo[popped] + 1
            queue.append(int(popped / 3))

    if popped % 2 == 0:
        if memo[int(popped / 2)] == 0:
            memo[int(popped / 2)] = memo[popped] + 1
            queue.append(int(popped / 2))

    if memo[popped - 1] == 0:
        memo[popped - 1] = memo[popped] + 1
        queue.append(popped - 1)

print(memo[1])

# p.220 개미 전사 #######################################################################################################

# def recursion(array):
#     if len(array) == 3:
#         a = array[0] + array[2]
#         b = array[1]
#     elif len(array) == 2:
#         a = array[0]
#         b = array[1]
#     else:
#         a = array[0] + recursion(array[2:])
#         b = recursion(array[1:])
#
#     return max(a, b)


# n = int(input())
# warehouse = list(map(int, input().split()))
#
# print(recursion(warehouse))

n = int(input())
array = list(map(int, input().split()))

d = [0] * n

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])

# p.223 바닥 공사 #######################################################################################################

n = int(input())

d = [0] * (n + 1)

d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])

# p.226 효율적인 화폐 구성 ################################################################################################

n, m = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(1, m + 1):
    for coin in coins:
        if i >= coin and d[i - coin] != -1:
            d[i] = min(d[i], d[i - coin] + 1)

print(d[m]) if d[m] != 10001 else print(-1)

########################################################################################################################
