def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5] * 2000
    one = one[:len(answers)]
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    two = two[:len(answers)]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    three = three[:len(answers)]
    
    counts = [0] * 3
    for i in range(len(answers)):
        if answers[i] == one[i]:
            counts[0] += 1
        if answers[i] == two[i]:
            counts[1] += 1
        if answers[i] == three[i]:
            counts[2] += 1
    
    best = max(counts)
    for index, count in enumerate(counts):
        if count == best:
            answer.append(index + 1)
    
    return answer
