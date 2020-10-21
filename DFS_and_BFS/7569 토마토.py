from collections import deque


def bfs(box):
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    queue = deque()

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 1:
                    queue.append((i, j, k))
                    ripe[i][j][k] = True

    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if box[nz][nx][ny] == 0 and ripe[nz][nx][ny] is False:
                    queue.append((nz, nx, ny))
                    box[nz][nx][ny] = box[z][x][y] + 1
                    ripe[nz][nx][ny] = True

    days = 0

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    return -1

                days = max(days, box[i][j][k])

    return days - 1


if __name__ == "__main__":
    m, n, h = map(int, input().split())
    box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    ripe = [[[False] * m for _ in range(n)] for _ in range(h)]

    print(bfs(box))
