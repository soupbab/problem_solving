def binary_search(array, target, start, end):
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        count = 1
        check = array[0]

        for i in array[1:]:
            if i - check >= mid:
                count += 1
                check = i

        if count >= target:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer


if __name__ == "__main__":
    n, c = map(int, input().split())
    house = []

    for _ in range(n):
        house.append(int(input()))

    house.sort()

    print(binary_search(house, c, 1, (house[-1] - house[0]) // (c - 1)))
