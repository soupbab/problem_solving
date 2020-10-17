import sys


def chess(board):
    pattern_1 = "WBWBWBWB"
    pattern_2 = "BWBWBWBW"
    cnt_1 = 0
    cnt_2 = 0

    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if board[i][j] != pattern_1[j]:
                    cnt_1 += 1
            else:
                if board[i][j] != pattern_2[j]:
                    cnt_1 += 1

    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if board[i][j] != pattern_2[j]:
                    cnt_2 += 1
            else:
                if board[i][j] != pattern_1[j]:
                    cnt_2 += 1

    return min(cnt_1, cnt_2)


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().rstrip().split())
    full_board = [sys.stdin.readline().rstrip() for _ in range(n)]

    counts = []

    for i in range(n-7):
        for j in range(m-7):
            board = [full_board[k][j:j+8] for k in range(i, i+8)]

            counts.append(chess(board))

    print(min(counts))
