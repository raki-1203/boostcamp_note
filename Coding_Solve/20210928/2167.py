import sys
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 누적합 리스트를 미리 만들어 놓음
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            prefix_sum[i][j] = \
                board[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

    K = int(input())
    for _ in range(K):
        i, j, x, y = map(int, input().split())
        print(prefix_sum[x][y] - prefix_sum[x][j - 1] - prefix_sum[i - 1][y] + prefix_sum[i - 1][j - 1])


if __name__ == "__main__":
    solution()
