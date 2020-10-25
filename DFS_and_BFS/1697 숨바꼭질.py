from collections import deque


def bfs(n, k):
    queue = deque([])
    queue.append((n, 0))
    check = [False] * 100001

    while queue[0][0] != k:
        popped = queue.popleft()
        number, count = popped[0], popped[1]
        check[number] = True
        move_minus, move_plus, teleport = number - 1, number + 1, number * 2

        if move_minus >= 0 and check[move_minus] is False:
            queue.append((move_minus, count + 1))
            check[move_minus] = True

        if move_plus <= 100000 and check[move_plus] is False:
            queue.append((move_plus, count + 1))
            check[move_plus] = True

        if teleport <= 100000 and check[teleport] is False:
            queue.append((teleport, count + 1))
            check[teleport] = True

    return queue[0][1]


if __name__ == "__main__":
    n, k = map(int, input().split())

    print(bfs(n, k))
