# p.149 음료수 얼려 먹기 ##################################################################################################


def make_ice(i, j, frame):
    frame[i][j] = 2
    neighbors = []

    if i > 0:
        neighbors.append((i-1, j))
    if i < n-1:
        neighbors.append((i+1, j))
    if j > 0:
        neighbors.append((i, j-1))
    if j < m-1:
        neighbors.append((i, j+1))

    for neighbor in neighbors:
        if frame[neighbor[0]][neighbor[1]] == 0:
            make_ice(neighbor[0], neighbor[1], frame)


if __name__ == "__main__":
    n, m = map(int, input().split())
    frame = [list(map(int, input())) for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if frame[i][j] == 0:
                make_ice(i, j, frame)
                count += 1

    print(count)

# p.152 미로 탈출 #######################################################################################################

from collections import deque


def find_path(maze):
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        next = []

        if x > 0:
            next.append((x-1, y))
        if x < n-1:
            next.append((x+1, y))
        if y > 0:
            next.append((x, y-1))
        if y < m-1:
            next.append((x, y+1))

        for i in next:
            if maze[i[0]][i[1]] == 1 and visited[i[0]][i[1]] is False:
                queue.append(i)
                maze[i[0]][i[1]] = maze[x][y] + 1
                visited[i[0]][i[1]] = True

    return maze[n-1][m-1]


if __name__ == "__main__":
    n, m = map(int, input().split())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    print(find_path(maze))

########################################################################################################################
