import sys
import heapq


def abs_heap(array, number):
    if number > 0:
        heapq.heappush(array, (number + 0.5, number))
    elif number < 0:
        heapq.heappush(array, (-number, number))
    else:
        if array:
            return print(heapq.heappop(array)[1])
        else:
            return print(0)


n = int(input())

q = []
for _ in range(n):
    abs_heap(q, int(sys.stdin.readline().rstrip()))
