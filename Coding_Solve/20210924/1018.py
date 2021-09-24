import sys
input = sys.stdin.readline


def solution():
    min_cnt = 99999999
    for i in range(N - 7):
        for j in range(M - 7):
            cnt_W = 0
            cnt_B = 0
            for ii in range(i, i+8):
                for jj in range(j, j+8):
                    if (ii + jj) % 2 == 0:
                        if board[ii][jj] == 'W':
                            cnt_B += 1
                        if board[ii][jj] == 'B':
                            cnt_W += 1
                    else:
                        if board[ii][jj] == 'B':
                            cnt_B += 1
                        if board[ii][jj] == 'W':
                            cnt_W += 1

            cnt = min(cnt_W, cnt_B)
            if min_cnt > cnt:
                min_cnt = cnt

    print(min_cnt)


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]
    solution()
