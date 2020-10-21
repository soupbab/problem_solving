from collections import deque


def find_path(maze):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and visited[nx][ny] is False:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
                visited[nx][ny] = True

    return maze[n-1][m-1]


if __name__ == "__main__":
    n, m = map(int, input().split())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    print(find_path(maze))
