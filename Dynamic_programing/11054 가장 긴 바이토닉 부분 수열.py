# def binary_search(array, target, start, end):
#     index = 0
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if array[mid] >= target:
#             index = mid
#             end = mid - 1
#         else:
#             start = mid + 1
#
#     return index
#
#
# n = int(input())
# sequence = list(map(int, input().split()))
#
# answer = []
#
# for i in range(n):
#     dp_increase = [0]
#
#     for number in sequence[:i]:
#         if dp_increase[-1] < number:
#             dp_increase.append(number)
#         else:
#             dp_increase[binary_search(dp_increase, number, 0, len(dp_increase) - 1)] = number
#
#     dp_decrease = [0]
#
#     for number in reversed(sequence[i:]):
#         if dp_decrease[-1] < number:
#             dp_decrease.append(number)
#         else:
#             dp_decrease[binary_search(dp_decrease, number, 0, len(dp_decrease) - 1)] = number
#
#     if dp_increase[-1] == dp_decrease[-1]:
#         answer.append(len(dp_increase) + len(dp_decrease) - 3)
#     else:
#         answer.append(len(dp_increase) + len(dp_decrease) - 2)
#
# print(max(answer))

########################################################################################################################
# https://suri78.tistory.com/7

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
increase = [1 for _ in range(N)]
decrease = [1 for _ in range(N)]
result = [0 for _ in range(N)]

# increase
for i in range(N):
    for j in range(i):
        if A[i] > A[j] and increase[i] < increase[j] + 1:
            increase[i] = increase[j] + 1

# decrease
for i in range(N-1, -1, -1):
    for j in range(i + 1, N):
        if A[i] > A[j] and decrease[i] < decrease[j] + 1:
            decrease[i] = decrease[j] + 1
    result[i] = decrease[i] + increase[i] - 1

print(max(result))

