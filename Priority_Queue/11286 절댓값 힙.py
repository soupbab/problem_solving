import sys
import heapq


def abs_heap(array, number):
    if number != 0:
        heapq.heappush(array, number)
    else:
        if array:
            return print(heapq.heappop(array))
        else:
            return print(0)


n = int(input())

q = []
for _ in range(n):
    abs_heap(q, int(sys.stdin.readline().rstrip()))
