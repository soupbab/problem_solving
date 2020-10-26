# p.197 부품 찾기 ########################################################################################################


def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(input())
numbers = sorted(list(map(int, input().split())))
m = int(input())
requests = list(map(int, input().split()))

if __name__ == "__main__":
    for item in requests:
        result = binary_search(numbers, item, 0, n-1)

        print("no", end=" ") if result is None else print("yes", end=" ")

# p.201 떡볶이 떡 만들기 #################################################################################################


def binary_search_2(array, target, start, end):
    temp = 0

    while start <= end:
        mid = (start + end) // 2
        product = 0

        for rice_cake in rice_cakes:
            if rice_cake > mid:
                product += rice_cake - mid

        if product < target:
            end = mid - 1
        else:
            temp = mid
            start = mid + 1

    return temp


if __name__ == "__main__":
    n, m = map(int, input().split())
    rice_cakes = sorted(list(map(int, input().split())))
    height = max(rice_cakes)
    cutter = list(range(0, height))

    print(binary_search_2(cutter, m, 0, height))

########################################################################################################################
