from collections import deque
from sys import stdin
input = stdin.readline

def bfs(graph):
    visited = [[0] * N for _ in range(N)]
    D = [(0, 1), (1, 0)]
    queue = deque([(0, 0)])
    result = 'Hing'

    while queue:
        x, y = queue.popleft()
        for d in D:
            nx = x + d[0] * graph[x][y]
            ny = y + d[1] * graph[x][y]
            if nx >= N or ny >= N:
                continue
            if graph[nx][ny] == -1:
                return 'HaruHaru'
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    return result

if __name__ == "__main__":
    N = int(input())
    graph = [[int(n) for n in input().split()] for _ in range(N)]
    print(bfs(graph))
    