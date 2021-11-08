from collections import deque
import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]

    visited = [[False] * M for _ in range(N)]

    stack = deque()
    stack.append((0, 0, 1))  # row, col, cnt
    visited[0][0] = True

    result = []
    while stack:
        row, col, cnt = stack.popleft()

        for D in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = row + D[0]
            nc = col + D[1]

            if nr == N - 1 and nc == M - 1:
                result.append(cnt + 1)

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and board[nr][nc] == '1':
                visited[nr][nc] = True
                stack.append((nr, nc, cnt + 1))

    print(min(result))


if __name__ == '__main__':
    solution()
