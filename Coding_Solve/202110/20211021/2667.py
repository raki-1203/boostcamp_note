import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]

    cnt = 0
    queue = deque()

    for i in range(N):
        for j in range(N):
            # 아파트인 경우 1, 2, 3, ...  이렇게 숫자를 줘가면서 단지를 파악
            if board[i][j] == '1':
                cnt += 1
                queue.append((i, j))
                board[i][j] = cnt

                while queue:
                    r, c = queue.pop()
                    # 상, 하, 좌, 우 의 아파트들 모두 탐색해서 있으면 같은 단지로 표시
                    for D in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr = r + D[0]
                        nc = c + D[1]
                        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == '1':
                            board[nr][nc] = cnt
                            queue.append((nr, nc))

    new_board = []
    for i in range(N):
        new_board.extend(board[i])

    apt_cnt = []
    for i in range(1, cnt + 1):
        apt_cnt.append(new_board.count(i))

    print(cnt)
    apt_cnt.sort()
    for i in range(len(apt_cnt)):
        print(apt_cnt[i])


if __name__ == '__main__':
    solution()
