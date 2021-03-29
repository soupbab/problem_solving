def solution(people, limit):
    answer = 0
    people.sort()
    light_index = 0
    heavy_index = len(people) - 1
    
    while light_index < heavy_index:
        if people[light_index] + people[heavy_index] <= limit:
            light_index += 1

        answer += 1
        heavy_index -= 1 
            
    if light_index == heavy_index:
        answer += 1
    
    return answer
