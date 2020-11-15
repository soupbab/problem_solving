import sys
import heapq

n = int(input())

q = []
array = []

for i in range(n):
    heapq.heappush(q, int(sys.stdin.readline().rstrip()))

for i in range(n):
    array.append(heapq.heappop(q))
    print(array[i // 2])
