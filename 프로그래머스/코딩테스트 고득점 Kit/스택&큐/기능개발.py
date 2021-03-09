import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque([math.ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)])    
    now = 0
    count = 0
    while days:
        day = days.popleft()
        now = max(now, day)
        count += 1
        if not days:
            answer.append(count)
        elif day < days[0] and now < days[0]:
            answer.append(count)
            count = 0
    
    return answer
