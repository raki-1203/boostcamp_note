import sys

input = sys.stdin.readline


def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp = sorted(temp, reverse=True)
                stack += temp

    print(*visited)


def BFS(graph, root):
    visited = []
    queue = [root]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp = sorted(temp)
                queue += temp

    print(*visited)


def solution():
    N, M, V = map(int, input().split())

    graph = {}

    for _ in range(M):
        a, b = map(int, input().split())
        # 입력으로 주어지는 간선은 양방향이다.
        # 위 문구때문에 왼쪽에서 오른쪽 방향 뿐만 아니라 오른쪽에서 왼쪽으로의 방향도 graph 에 추가
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)

        if b not in graph:
            graph[b] = [a]
        elif a not in graph[b]:
            graph[b].append(a)

    DFS(graph, V)
    BFS(graph, V)


if __name__ == '__main__':
    solution()
