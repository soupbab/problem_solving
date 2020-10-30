n = int(input())
point = []
for _ in range(n):
    point.append(int(input()))

dp = [0] * n

dp[0] = point[0]
if n > 1:
    dp[1] = dp[0] + point[1]
if n > 2:
    dp[2] = max(point[0], point[1]) + point[2]
for i in range(3, n):
    dp[i] = max(dp[i - 3] + point[i - 1], dp[i - 2]) + point[i]

print(dp[n - 1])
