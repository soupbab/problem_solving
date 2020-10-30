n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

dp = [[0] * i for i in range(1, n + 1)]

dp[0][0] = nums[0][0]
for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i - 1][0] + nums[i][j]
        elif j < len(dp[i]) - 1:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + nums[i][j]
        else:
            dp[i][j] = dp[i - 1][j - 1] + nums[i][j]

print(max(dp[n - 1]))
