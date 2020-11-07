n = int(input())
numbers = list(map(int, input().split()))

dp = [-1000] * len(numbers)

dp[0] = numbers[0]
for i in range(1, len(numbers)):
    dp[i] = max(numbers[i], dp[i - 1] + numbers[i])

print(max(dp))
