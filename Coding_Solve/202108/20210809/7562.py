from collections import deque
from sys import stdin
input = stdin.readline

def bfs():
    l = int(input())
    x, y = map(int, input().split())
    tx, ty = map(int, input().split())

    D = [(1, 2), (2, 1), (-1, 2), (-2, 1), 
        (1, -2), (2, -1), (-1, -2), (-2, -1)]

    visited = [[0] * l for _ in range(l)]
    visited[x][y] == 1
    cnt = 0
    queue = deque([(x, y, cnt)])

    while queue:
        x, y, cnt = queue.popleft()

        if x == tx and y == ty:
            return cnt

        for d in D:
            nx, ny = x + d[0], y + d[1]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny, cnt + 1))
    
    return cnt


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(bfs())
