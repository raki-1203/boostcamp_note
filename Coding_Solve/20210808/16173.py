from collections import deque
from sys import stdin
input = stdin.readline

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                queue += temp

    return len(visited) - 1


if __name__ == "__main__":
    N = int(input())
    graph = [[int(n) for n in input().split()] for _ in range(N)]
    print(bfs(graph))
    