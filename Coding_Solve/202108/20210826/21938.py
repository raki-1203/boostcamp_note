from collections import deque
from sys import stdin
input = stdin.readline

def bfs(x, y):
    visited[x][y] = True
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()

        for D in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + D[0]
            ny = y + D[1]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and object_arr[nx][ny] == 255:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

            
if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    T = int(input())

    # 물체가 있는지 없는지 배열
    object_arr = []
    for row in arr:
        temp = []
        for i in range(M):
            if sum(row[3 * i:3 * (i + 1)]) / 3 < T:
                temp.append(0)
            else:
                temp.append(255)
        object_arr.append(temp)

    # 방문했는지 배열
    visited = [[False] * M for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            # 만약 물체가 있고 방문한적이 없으면
            if object_arr[i][j] == 255 and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)
       
