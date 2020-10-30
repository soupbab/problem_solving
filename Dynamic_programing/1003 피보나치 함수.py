def fibonacci(n, array):
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    else:
        if array[n] == [0, 0]:
            a, b = fibonacci(n - 1, array)
            c, d = fibonacci(n - 2, array)
            array[n] = [a + c, b + d]
        return array[n][0], array[n][1]


t = int(input())
case = []
for _ in range(t):
    case.append(int(input()))

numbers = [[0, 0]] * 41

numbers[0] = [1, 0]
numbers[1] = [0, 1]
for i in case:
    fibonacci(i, numbers)
    print(numbers[i][0], numbers[i][1])
