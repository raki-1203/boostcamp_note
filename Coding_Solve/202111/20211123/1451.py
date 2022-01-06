import sys
input = sys.stdin.readline


def get_sum(dp, x1, y1, x2, y2):
    return dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]


def solution():
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, list(input().strip()))))

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = board[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

    answer = 0

    # 첫번째 경우: 전체 직사각형을 세로로만 분할한 경우
    for i in range(1, M - 1):
        for j in range(i + 1, M):
            r1 = get_sum(dp, 1, 1, N, i)
            r2 = get_sum(dp, 1, i+1, N, j)
            r3 = get_sum(dp, 1, j+1, N, M)
            if answer < r1 * r2 * r3:
                answer = r1 * r2 * r3

    # 두번째 경우: 전체 직사각형을 가로로만 분할한 경우
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            r1 = get_sum(dp, 1, 1, i, M)
            r2 = get_sum(dp, i+1, 1, j, M)
            r3 = get_sum(dp, j+1, 1, N, M)
            if answer < r1 * r2 * r3:
                answer = r1 * r2 * r3

    # 세번째 경우: 전체 세로 분할 후 우측 가로 분할한 경우
    for i in range(1, M):
        for j in range(1, N):
            r1 = get_sum(dp, 1, 1, N, i)
            r2 = get_sum(dp, 1, i+1, j, M)
            r3 = get_sum(dp, j+1, i+1, N, M)
            if answer < r1 * r2 * r3:
                answer = r1 * r2 * r3

    # 네번째 경우: 전체 세로 분할 후 좌측 가로 분할한 경우
    for i in range(1, N):
        for j in range(1, M):
            r1 = get_sum(dp, 1, 1, i, j)
            r2 = get_sum(dp, i+1, 1, N, j)
            r3 = get_sum(dp, 1, j+1, N, M)
            if answer < r1 * r2 * r3:
                answer = r1 * r2 * r3

    # 다섯번째 경우: 전체 가로 분할 후 하단 세로 분할한 경우
    for i in range(1, N):
        for j in range(1, M):
            r1 = get_sum(dp, 1, 1, i, M)
            r2 = get_sum(dp, i+1, 1, N, j)
            r3 = get_sum(dp, i+1, j+1, N, M)
            if answer < r1 * r2 * r3:
                answer = r1 * r2 * r3

    # 여섯번째 경우: 전체 가로 분할 후 상단 세로 분할한 경우
    for i in range(1, N):
        for j in range(1, M):
            r1 = get_sum(dp, 1, 1, i, j)
            r2 = get_sum(dp, 1, j+1, i, M)
            r3 = get_sum(dp, i+1, 1, N, M)
            if answer < r1 * r2 * r3:
                answer = r1 * r2 * r3

    print(answer)


if __name__ == '__main__':
    solution()