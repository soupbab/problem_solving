if __name__ == "__main__":
    n = input()
    numbers = [0] * 10

    for i in n:
        numbers[int(i)] += 1

    for idx, number in enumerate(numbers[::-1]):
        for _ in range(number):
            print(9-idx, end="")
