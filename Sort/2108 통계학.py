import sys

if __name__ == "__main__":
    n = int(input())
    array = [0] * 8001
    numbers = []
    most_frequent_values = []

    for _ in range(n):
        array[int(sys.stdin.readline().rstrip()) + 4000] += 1

    frequency = max(array)

    for idx, number in enumerate(array):
        if number == frequency:
            most_frequent_values.append(idx - 4000)

        for _ in range(number):
            numbers.append(idx - 4000)

    print("%.f" % float(sum(numbers) / len(numbers)))
    print(numbers[int(len(numbers) / 2)])
    print(most_frequent_values[0]) if len(most_frequent_values) == 1 else print(most_frequent_values[1])
    print(numbers[-1] - numbers[0])
