def binary_search(array, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if array[mid] == target:
        return 1
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


if __name__ == "__main__":
    n = int(input())
    numbers = sorted(list(map(int, input().split())))
    m = int(input())
    targets = list(map(int, input().split()))

    for target in targets:
        print(binary_search(numbers, target, 0, n-1))
