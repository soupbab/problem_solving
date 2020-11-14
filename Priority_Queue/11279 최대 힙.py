import sys
import heapq


def max_heap(array, number):
    if number > 0:
        heapq.heappush(array, -number)
    else:
        if len(array) == 0:
            return print(0)
        else:
            return print(-heapq.heappop(array))


n = int(input())

q = []
for _ in range(n):
    max_heap(q, int(sys.stdin.readline().rstrip()))
