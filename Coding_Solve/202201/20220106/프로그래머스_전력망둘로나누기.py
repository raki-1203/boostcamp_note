def solution(n, wires):
    answer = -1

    graph = [[0] * n for _ in range(n)]
    for a, b in wires:
        graph[a - 1][b - 1] = graph[b - 1][a - 1] = 1

    min_cnt = 99
    for a, b in wires:
        graph[a - 1][b - 1] = graph[b - 1][a - 1] = 0

        visited = [True] * n
        visited[a-1] = False
        stack = [a - 1]
        cnt = 1
        while stack:
            node= stack.pop()
            for i, is_line in enumerate(graph[node]):
                if is_line and visited[i]:
                    stack.append(i)
                    visited[i] = False
                    cnt += 1
        a_cnt = cnt

        visited = [True] * n
        visited[b - 1] = False
        stack = [b - 1]
        cnt = 1
        while stack:
            node = stack.pop()
            for i, is_line in enumerate(graph[node]):
                if is_line and visited[i]:
                    stack.append(i)
                    visited[i] = False
                    cnt += 1
        b_cnt = cnt

        cnt = abs(a_cnt - b_cnt)
        min_cnt = min(cnt, min_cnt)

        graph[a - 1][b - 1] = graph[b - 1][a - 1] = 1

    answer = min_cnt

    return answer


if __name__ == '__main__':
    n = 9
    wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
    print(solution(n , wires))
