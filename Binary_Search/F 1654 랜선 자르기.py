def binary_search(array, target, start, end):
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        count = 0

        for i in array:
            count += i // mid

        if count >= target:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer


if __name__ == "__main__":
    k, n = map(int, input().split())
    wires = []

    for _ in range(k):
        wires.append(int(input()))

    max_length = sum(wires) // n

    print(binary_search(wires, n, 1, max_length))
