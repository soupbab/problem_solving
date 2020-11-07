# https://jay-ji.tistory.com/33

a = input()
b = input()

table = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            table[i + 1][j + 1] = table[i][j] + 1
        else:
            table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])

print(table[len(a)][len(b)])
