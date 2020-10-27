def binary_search(array, target, start, end):
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        length = 0

        for i in array:
            if i > mid:
                length += i - mid

        if length >= target:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer


if __name__ == "__main__":
    n, m = map(int, input().split())
    woods = list(map(int, input().split()))

    print(binary_search(woods, m, 1, max(woods)))
