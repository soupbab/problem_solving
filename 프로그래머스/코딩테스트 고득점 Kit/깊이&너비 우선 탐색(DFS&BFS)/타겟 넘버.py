from collections import deque, Counter

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append(0)
    for index, number in enumerate(numbers):
        for i in range(2 ** index):
            temp = q.popleft()
            q.append(temp + number)
            q.append(temp - number)
    
    counter = Counter(q)
    answer = counter[target]
            
    return answer
