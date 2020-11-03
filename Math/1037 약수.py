n = int(input())
numbers = sorted(list(map(int, input().split())))

if n == 1:
    print(numbers[0] ** 2)
else:
    print(numbers[0] * numbers[-1])
