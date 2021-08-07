from collections import deque
from sys import stdin
input = stdin.readline

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                stack += temp

    return len(visited) - 1

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
    graph = {}
    node = int(input())
    edge = int(input())
    start = 1 
    for i in range(edge):
        edge_info = input().split()
        n1, n2 = [int(n) for n in edge_info]
        if n1 not in graph:
            graph[n1] = [n2]
        elif n2 not in graph[n1]:
            graph[n1].append(n2)

        if n2 not in graph:
            graph[n2] = [n1]
        elif n1 not in graph[n2]:
            graph[n2].append(n1)

    print(dfs(graph, start))
    print(bfs(graph, start))
    