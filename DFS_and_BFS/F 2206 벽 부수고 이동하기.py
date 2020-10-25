# import sys
# import copy
# from collections import deque
#
#
# def bfs(data):
#     check_sheet = [[False] * m for _ in range(n)]
#     queue = deque([])
#     queue.append((0, 0))
#     check_sheet[0][0] = True
#     data[0][0] = 1
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#
#     while queue:
#         curr = queue.popleft()
#         x, y = curr[0], curr[1]
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < m:
#                 if data[nx][ny] == 0 and check_sheet[nx][ny] is False:
#                     queue.append((nx, ny))
#                     data[nx][ny] = data[x][y] + 1
#
#     return data[-1][-1] if data[-1][-1] != 0 else -1
#
#
# def find_path(maze):
#     distance = set()
#
#     for i in range(n):
#         for j in range(m):
#             if maze[i][j] == 1:
#                 changed_maze = copy.deepcopy(maze)
#                 changed_maze[i][j] = 0
#                 value = bfs(changed_maze)
#                 distance.add(value)
#
#                 if value == n + m - 1:
#                     return value
#
#     distance = sorted(list(distance))
#
#     if -1 in distance:
#         distance.pop(0)
#
#     return -1 if len(distance) == 0 else distance[0]

########################################################################################################################

import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(data):
    visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
    queue = deque([])
    queue.append((0, 0, 1))
    visit[0][0][1] = 1

    while queue:
        x, y, chance = queue.popleft()

        if x == n-1 and y == m-1:
            return visit[x][y][chance]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 0 and visit[nx][ny][chance] == 0:
                    visit[nx][ny][chance] = visit[x][y][chance] + 1
                    queue.append((nx, ny, chance))
                elif data[nx][ny] == 1 and chance == 1:
                    visit[nx][ny][0] = visit[x][y][chance] + 1
                    queue.append((nx, ny, 0))

    return -1


if __name__ == "__main__":
    n, m = map(int, input().split())
    maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

    print(bfs(maze))
