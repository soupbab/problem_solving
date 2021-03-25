def get_divisors(number):
    if number == 1:
        return [[1, 1]]
    
    numbers = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            numbers.append([number // i, i])            
    return numbers


def solution(brown, yellow):
    pairs = get_divisors(yellow)
    for column, row in pairs:
        if (column + 2) * (row + 2) - column * row == brown:
            return [column + 2, row + 2]
