def binary_search(array, target, start, end):
    index = 0

    while start <= end:
        mid = (start + end) // 2

        if array[mid] >= target:
            index = mid
            end = mid - 1
        else:
            start = mid + 1

    return index


n = int(input())
sequence = list(map(int, input().split()))

dp = []

dp.append(sequence[0])
for number in sequence[1:]:
    if dp[-1] < number:
        dp.append(number)
    else:
        dp[binary_search(dp, number, 0, len(dp) - 1)] = number

print(len(dp))
