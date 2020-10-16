import sys


def calculate(equation):
    splitted_by_minus = equation.split("-")
    merged_numbers = []

    for splitted_equation in splitted_by_minus:
        if "+" in splitted_equation:
            splitted_by_plus = list(map(int, splitted_equation.split("+")))
            merged_numbers.append(sum(splitted_by_plus))
        else:
            merged_numbers.append(int(splitted_equation))

    answer = 0

    if equation[0] == "-":
        answer -= merged_numbers[0]
    else:
        answer += merged_numbers[0]

    for i in range(1, len(merged_numbers)):
        answer -= merged_numbers[i]

    return answer


if __name__ == "__main__":
    equation = input()

    print(calculate(equation))
