from collections import deque
import sys
input = sys.stdin.readline


def solution():
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())

        board = [['0'] *  M for _ in range(N)]

        for _ in range(K):
            X, Y = map(int, input().split())
            board[Y][X] = '1'

        cnt = 0
        queue = deque()
        for i in range(N):
            for j in range(M):
                if board[i][j] == '1':
                    queue.append((i, j))
                    cnt += 1
                    board[i][j] = cnt
                    while queue:
                        r, c = queue.pop()

                        for D in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nr = r + D[0]
                            nc = c + D[1]
                            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == '1':
                                board[nr][nc] = cnt
                                queue.append((nr, nc))

        print(cnt)



if __name__ == '__main__':
    solution()