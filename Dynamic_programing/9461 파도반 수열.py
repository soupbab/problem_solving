t = int(input())
case = []
for _ in range(t):
    case.append(int(input()))

dp = [0, 1, 1, 1, 2, 2] + [0] * 95
for i in range(5, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

for i in case:
    print(dp[i])