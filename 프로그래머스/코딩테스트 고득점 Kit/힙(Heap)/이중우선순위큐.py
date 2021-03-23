import heapq

def solution(operations):
    heap = []
    for operation in operations:
        command, data = operation.split(" ")
        if command == "I":
            heapq.heappush(heap, int(data))
        elif command =="D" and heap:
            if data == "1":
                max_heap = list(map(lambda x: -x, heap))
                heapq.heapify(max_heap)
                heapq.heappop(max_heap)
                heap = list(map(lambda x: -x, max_heap))
                heapq.heapify(heap)
            else:
                heapq.heappop(heap)
    
    if heap:
        heap.sort()
        answer = [heap[-1], heap[0]]
    else:
        answer = [0, 0]
        
    return answer
