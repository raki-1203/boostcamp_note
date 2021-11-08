import sys
from collections import deque

input = sys.stdin.readline

def solution():
    M, N = map(int, input().split())
    board = []
    queue = deque([])

    for n in range(N):
        temp = list(map(int, input().split()))
        for m in range(M):
            if temp[m] == 1:
                queue.append([n, m])
        board.append(temp)

    dn = [1, -1, 0, 0]
    dm = [0, 0, 1, -1]

    while queue:
        n, m = queue.popleft()

        for i in range(4):
            nn = n + dn[i]
            nm = m + dm[i]

            if 0 <= nn < N and 0 <= nm < M and board[nn][nm] == 0:
                queue.append([nn, nm])
                board[nn][nm] = board[n][m] + 1

    day = 0
    for i in board:
        for j in i:
            if j == 0:
                print(-1)
                exit(0)
        day = max(day, max(i))

    print(day - 1)


if __name__ == '__main__':
    solution()