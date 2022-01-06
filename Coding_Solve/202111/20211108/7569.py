import sys
from collections import deque

input = sys.stdin.readline

def solution():
    M, N, H = map(int, input().split())

    queue = deque([])

    board = []
    for h in range(H):
        temp = []
        for n in range(N):
            temp.append(list(map(int, input().split())))
            for m in range(M):
                if temp[n][m] == 1:
                    queue.append([h, n, m])
        board.append(temp)

    dh = [1, -1, 0, 0, 0, 0]
    dn = [0, 0, 1, -1, 0, 0]
    dm = [0, 0, 0, 0, 1, -1]

    while queue:
        h, n, m = queue.popleft()

        for i in range(6):
            nh = h + dh[i]
            nn = n + dn[i]
            nm = m + dm[i]
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and board[nh][nn][nm] == 0:
                queue.append([nh, nn, nm])
                board[nh][nn][nm] = board[h][n][m] + 1

    day = 0
    for i in board:
        for j in i:
            for k in j:
                if k == 0:
                    print(-1)
                    exit(0)
            day = max(day, max(j))
    print(day - 1)


if __name__ == '__main__':
    solution()