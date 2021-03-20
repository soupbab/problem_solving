import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    
    for food in scoville:
        heapq.heappush(heap, food)
        
    while heap[0] < K:
        if len(heap) == 1:
            return -1
        
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        new = first + 2 * second
        heapq.heappush(heap, new)
        answer += 1
    
    return answer
