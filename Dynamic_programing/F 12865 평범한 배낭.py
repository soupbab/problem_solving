n, k = map(int, input().split())
items = []
for _ in range(n):
    items.append(list(map(int, input().split())))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n):
    for capacity in range(1, k + 1):
        if items[i][0] <= capacity:
            dp[i + 1][capacity] = max(dp[i][capacity - items[i][0]] + items[i][1], dp[i][capacity])
        else:
            dp[i + 1][capacity] = dp[i][capacity]

print(dp[n][k])

