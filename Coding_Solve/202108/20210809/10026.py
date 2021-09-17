import sys
sys.setrecursionlimit(20000)
from collections import deque
from sys import stdin
input = stdin.readline

def dfs(x, y):
    # 현재 색상 좌표를 방문해준다.
    visited[x][y] = 1
    current_color = graph[x][y]

    for d in D:
        nx = x + d[0]
        ny = y + d[1]

        if (0 <= nx < N) and (0 <= ny < N):
            # 방문한적 없고
            if visited[nx][ny] == 0:
                # 현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs로 넣어준다.
                if graph[nx][ny] == current_color:
                    dfs(nx, ny)


if __name__ == '__main__':
    N = int(input())
    graph = [[color for color in input().strip()] for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    D = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # 비적록색약 구분 구역수
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 방문하지 않은 좌표이면 dfs로 넣어준다.
            if visited[i][j] == 0:
                dfs(i, j)
                cnt += 1

    visited = [[0] * N for _ in range(N)]

    # G를 R로 바꾸어준다.
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'G':
                graph[i][j] = 'R'

    # 적록색약 구분 구역수
    rg_cb_cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                dfs(i, j)
                rg_cb_cnt += 1

    print(cnt, rg_cb_cnt)
    
