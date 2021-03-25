from itertools import permutations

def is_prime_number(number):
    if number == 0 or number == 1:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True
    

def solution(numbers):
    numbers_ = []
    for i in range(1, len(numbers) + 1):
        numbers_ += list(map(int, map("".join, permutations(numbers, i))))
    numbers_ = list(set(numbers_))

    answer = 0    
    for number in numbers_:
        if is_prime_number(number):
            answer += 1
    return answer
