a, b = map(int, input().split())

lcm = 0

for i in range(1, b + 1):
    if (a * i) % b == 0:
        lcm = a * i
        break

gcd = (a * b) // lcm

print(gcd)
print(lcm)
