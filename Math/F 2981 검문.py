n = int(input())

numbers = []
for _ in range(3):
    numbers.append(int(input()))

a = min(numbers)

for i in range(2, a + 1):
    mods = set()

    for number in numbers:
        mod = number % i
        mods.add(mod)

        if len(mods) > 1:
            break
    else:
        print(i, end=" ")
