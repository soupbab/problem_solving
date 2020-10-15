# p.110 상하좌우 ########################################################################################################

size = int(input())
moves = input().split()

x, y = 1, 1

for move in moves:
    if move == "L":
        if y > 1:
            y -= 1
    elif move == "R":
        if y < size:
            y += 1
    elif move == "U":
        if x > 1:
            x -= 1
    else:
        if x < size:
            x += 1

print(x, y)

# p.113 시각 ############################################################################################################

n = int(input())

cnt = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h)+str(m)+str(s):
                cnt += 1

print(cnt)

# p.115 왕실의 나이트 ####################################################################################################

location = list(input())

x, y = int(location[1]), ord(location[0]) - 96
cnt = 0

if x > 2 and y < 8: cnt += 1
if x > 1 and y < 7: cnt += 1
if x < 8 and y < 7: cnt += 1
if x < 7 and y < 8: cnt += 1
if x < 7 and y > 1: cnt += 1
if x < 8 and y > 2: cnt += 1
if x > 1 and y > 2: cnt += 1
if x > 2 and y > 1: cnt += 1

print(cnt)

# p.118 게임 개발 #######################################################################################################

n, m = map(int, input().split())
x, y, d = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
turn_cnt = 0
move_cnt = 1

while True:
    game_map[x][y] = 2

    if d == 0:
        d = 3
    else:
        d -= 1
    turn_cnt += 1

    nx = x + dx[d]
    ny = y + dy[d]

    if game_map[nx][ny] == 0:
        x = nx
        y = ny
        move_cnt += 1
        turn_cnt = 0

    if turn_cnt == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if game_map[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny
            turn_cnt = 0

print(move_cnt)

########################################################################################################################
