import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(N)]

    visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visit[0][0][1] = 1  # 벽을 한번 부술 수 있는 상태에서 시작

    queue = deque([])
    queue.append([0, 0, 1])  # row, col, flag

    while queue:
        r, c, flag = queue.popleft()

        if r == (N - 1) and c == (M - 1):
            print(visit[r][c][flag])
            return

        for D in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = r + D[0]
            nc = c + D[1]

            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 1 and flag:  # 벽을 만나고 벽을 한번 부술 수 있는 경우
                    queue.append([nr, nc, 0])
                    visit[nr][nc][0] = visit[r][c][flag] + 1
                elif board[nr][nc] == 0 and visit[nr][nc][flag] == 0:  # 벽이 없고 방문한적이 없는 경우
                    queue.append([nr, nc, flag])
                    visit[nr][nc][flag] = visit[r][c][flag] + 1

    print(-1)


if __name__ == '__main__':
    solution()