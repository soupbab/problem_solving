# https://developmentdiary.tistory.com/354

def binary_search(array_size, target, start, end):
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        count = 0

        for i in range(1, n+1):
            count += min(mid//i, array_size)

        if count >= target:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    # a = [[i*j for i in range(1, n+1)] for j in range(1, n+1)]
    # b = [a[i][j] for i in range(n) for j in range(n)]

    print(binary_search(n, k, 1, k))
