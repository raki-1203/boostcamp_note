from collections import deque
from sys import stdin
input = stdin.readline

def bfs(x, y):
    D = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    queue = deque([(x, y)])
    current_color = graph[x][y]

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for d in D:
            nx, ny = x + d[0], y + d[1]

            if (0 <= nx < N) and (0 <= ny < N):
                if visited[nx][ny] == 0:
                    if graph[nx][ny] == current_color:
                        queue.append((nx, ny))

    return
                    
    
if __name__ == '__main__':
    N = int(input())
    graph = [[color for color in input().strip()] for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs(i, j)
                cnt += 1

    # G를 R로 바꾸어준다.
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'G':
                graph[i][j] = 'R'
    visited = [[0] * N for _ in range(N)]
    rg_cb_cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs(i, j)
                rg_cb_cnt += 1
            
    print(cnt, rg_cb_cnt)
    
