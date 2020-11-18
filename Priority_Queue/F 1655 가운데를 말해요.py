import sys
import heapq

n = int(input())

max_heap = []
min_heap = []

for i in range(n):
    data = int(sys.stdin.readline().rstrip())

    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-data, data))
    else:
        heapq.heappush(min_heap, data)

    if min_heap and max_heap[0][1] > min_heap[0]:
        temp_max = heapq.heappop(max_heap)[1]
        temp_min = heapq.heappop(min_heap)

        heapq.heappush(min_heap, temp_max)
        heapq.heappush(max_heap, (-temp_min, temp_min))

    print(max_heap[0][1])
