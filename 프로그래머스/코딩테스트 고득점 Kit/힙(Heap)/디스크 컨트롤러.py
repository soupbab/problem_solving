import heapq

def solution(jobs):
    length = len(jobs)
    answer = 0
    time = 0
    
    jobs.sort(key=lambda x: x[1])
    jobs.sort(key=lambda x: x[0])
    
    heap = []
    while jobs or heap:
        jobs_ = jobs.copy()
        for job in jobs_:
            request_time, necessary_time = job
            if request_time <= time:
                jobs.remove(job)
                heapq.heappush(heap, [necessary_time, request_time])
                
        if not heap:
            fastest = jobs.pop(0)
            heapq.heappush(heap, reversed(fastest))
            
        task = list(heapq.heappop(heap))
        time = max(time, task[1])
        time += task[0]
        answer += time - task[1]
    
    answer //= length
    return answer
