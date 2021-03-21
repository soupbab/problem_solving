def solution(n, lost, reserve):
    
    
    lost_check = lost.copy()
    for lost_number in lost_check:
        if lost_number in reserve:
            reserve.remove(lost_number)
            lost.remove(lost_number)
            
    lost_check = lost.copy()
    for lost_number in lost_check:
        if (lost_number - 1) in reserve:
            reserve.remove(lost_number - 1)
            lost.remove(lost_number)            
        elif (lost_number + 1) in reserve:
            reserve.remove(lost_number + 1)
            lost.remove(lost_number)

    answer = n - len(lost)
    return answer
