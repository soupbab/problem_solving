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

answer = []

for i in range(n):
    dp_increase = [0]

    for number in sequence[:i]:
        if dp_increase[-1] < number:
            dp_increase.append(number)
        else:
            dp_increase[binary_search(dp_increase, number, 0, len(dp_increase) - 1)] = number

    dp_decrease = [0]

    for number in reversed(sequence[i:]):
        if dp_decrease[-1] < number:
            dp_decrease.append(number)
        else:
            dp_decrease[binary_search(dp_decrease, number, 0, len(dp_decrease) - 1)] = number

    if dp_increase[-1] == dp_decrease[-1]:
        answer.append(len(dp_increase) + len(dp_decrease) - 3)
    else:
        answer.append(len(dp_increase) + len(dp_decrease) - 2)

print(max(answer))
