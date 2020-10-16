n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

cnt = 0
i = -1

while k > 0:
    a, b = divmod(k, coins[i])
    cnt += a
    k = b
    i -= 1

print(cnt)