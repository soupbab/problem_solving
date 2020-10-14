# 1096 #################################################################################################################

base = [[0 for _ in range(19)] for _ in range(19)]
cnt = int(input())
for _ in range(cnt):
    x, y = map(int, input().split())
    base[x - 1][y - 1] = 1
for row in base:
    for val in row:
        print(val, end=" ")
    print()

# 1097 #################################################################################################################


def flip(a):
    return "1" if a == "0" else "0"


base = []
for _ in range(19):
    base.append(input().split())
cnt = int(input())
for _ in range(cnt):
    x, y = map(int, input().split())
    for i in range(19):
        base[i][y - 1] = flip(base[i][y - 1])
        base[x - 1][i] = flip(base[x - 1][i])
for row in base:
    for val in row:
        print(val, end=" ")
    print()

# 1098 #################################################################################################################

h, w = map(int, input().split())
base = [[0 for _ in range(w)] for _ in range(h)]
n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    for l_ in range(l):
        if d == 0:
            base[x - 1][y + l_ - 1] = 1
        else:
            base[x + l_ - 1][y - 1] = 1
for row in base:
    for val in row:
        print(val, end=" ")
    print()

# 1099 #################################################################################################################

map_ = []
for _ in range(10):
    map_.append(input().split())
r, c = 1, 1
if map_[r][c] == "2":
    map_[r][c] = "9"
else:
    while True:
        map_[r][c] = "9"
        if map_[r][c + 1] == "0":
            c += 1
        elif map_[r][c + 1] == "1":
            if map_[r + 1][c] == "0":
                r += 1
            elif map_[r + 1][c] == "1":
                break
            else:
                map_[r + 1][c] = "9"
                break
        else:
            map_[r][c + 1] = "9"
            break
for row in map_:
    for val in row:
        print(val, end=" ")
    print()

########################################################################################################################
