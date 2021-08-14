from collections import deque
from sys import stdin
input = stdin.readline

def solution(N, arr):
    # 가장 많은 선배를 만날 수 있는 시작 번호
    max_i = 0
    # 가장 방문 수
    max_visited = 0
    for i in range(1, N + 1):
        # 방문을 기록할 array
        visited = [0] * (N + 1)
        visited[i] = 1
        # 선배가 알려준 다음 선배번호
        ans = arr[i]
        
        queue = deque([(i, ans)])

        while queue:
            i, ans = queue.popleft()

            # 만약 방문을 안한 선배면
            if visited[ans] == 0:
                visited[ans] = 1
                ans = arr[ans]
                queue.append((i, ans))
                
        if max_visited < sum(visited):
            max_visited = sum(visited)
            max_i = i

    return max_i

        
if __name__ == '__main__':
    N = int(input())
    arr = [0] + [int(input()) for _ in range(N)]
    print(solution(N, arr))
