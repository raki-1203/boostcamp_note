import sys
from collections import deque

input = sys.stdin.readline


def BFS(graph, V):
    visited = [-1] * (V + 1)
    queue = deque()
    for i in range(1, V + 1):
        if visited[i] == -1:
            visited[i] = True
            queue.append((i, True))
            while queue:
                x, subsetNum = queue.popleft()
                for now in graph[x]:
                    if visited[now] == -1:
                        visited[now] = not (subsetNum)
                        queue.append((now, not (subsetNum)))
                    else:
                        if visited[now] == subsetNum:
                            return 'NO'
    return 'YES'

def solution():
    K = int(input())

    for _ in range(K):
        V, E = map(int, input().split())
        graph = [[] for _ in range(V + 1)]
        for _ in range(E):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        print(BFS(graph, V))


if __name__ == '__main__':
    solution()