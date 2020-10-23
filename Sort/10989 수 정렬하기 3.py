import sys

if __name__ == "__main__":
    n = int(input())
    numbers = [0] * 10001

    for _ in range(n):
        numbers[int(sys.stdin.readline().rstrip())] += 1

    for idx, num in enumerate(numbers):
        for _ in range(num):
            print(idx)

