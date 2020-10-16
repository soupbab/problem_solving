import sys


def withdraw(times):
    total_sum = 0
    time_sum = 0

    for time in times:
        time_sum += time
        total_sum += time_sum

    return total_sum


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    times = list(map(int, sys.stdin.readline().rstrip().split()))

    times.sort()

    print(withdraw(times))
