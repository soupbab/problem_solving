from collections import deque

def solution(priorities, location):
    q = deque([(index, priority) for index, priority in enumerate(priorities)])        
    count = 0
    
    while q:
        max_priority = max(q, key=lambda x: x[1])
        items = q.popleft()
        
        if items == max_priority:
            count += 1
            if items[0] == location:
                break
        else:
            q.append(items)
    
    return count
