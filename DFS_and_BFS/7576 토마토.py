from collections import deque


def bfs(box):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j))
                ripe[i][j] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == 0 and ripe[nx][ny] is False:
                    queue.append((nx, ny))
                    box[nx][ny] = box[x][y] + 1
                    ripe[nx][ny] = True

    days = 0

    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return -1

            days = max(days, box[i][j])

    return days - 1


if __name__ == "__main__":
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    ripe = [[False] * m for _ in range(n)]

    print(bfs(box))
