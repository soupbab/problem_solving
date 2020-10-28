# https://claude-u.tistory.com/441

def binary_search(array, number, start, end):
    index = 0

    while start <= end:
        mid = (start + end) // 2

        if array[mid] >= number:
            index = mid
            end = mid - 1
        else:
            start = mid + 1

    return index


if __name__ == "__main__":
    n = int(input())
    sequence = list(map(int, input().split()))
    dp = [0]

    for i in sequence:
        if i > dp[-1]:
            dp.append(i)
        else:
            idx = binary_search(dp, i, 1, len(dp) - 1)
            dp[idx] = i

    print(len(dp) - 1)
