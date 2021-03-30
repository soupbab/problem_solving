def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[0])
    
    temp = []
    temp.append(routes[0])
    min_end = routes[0][1]
    
    for route in routes[1:]:
        if min_end < route[0]:
            answer += 1
            temp = []
            min_end = 30000
            
        temp.append(route)
        min_end = min(min_end, route[1])
        
    if temp:
        answer += 1
        
    return answer
