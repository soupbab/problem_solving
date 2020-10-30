n = int(input())
count = [1000001] * (n + 1)

count[1] = 0
for i in range(2, n + 1):
    if i % 3 == 0:
        count[i] = min(count[i], count[i // 3] + 1)

    if i % 2 == 0:
        count[i] = min(count[i], count[i // 2] + 1)

    count[i] = min(count[i], count[i - 1] + 1)

print(count[n])
