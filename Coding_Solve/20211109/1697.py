import sys
from collections import deque

input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())
    visit = [0] * (100000 + 1)

    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()

        if x == K:
            print(visit[x])
            exit(0)

        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx <= 100000 and not visit[nx]:
                visit[nx] = visit[x] + 1
                queue.append(nx)


if __name__ == '__main__':
    solution()