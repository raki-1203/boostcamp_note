from collections import deque
from sys import stdin
input = stdin.readline

def bfs(xy_info):
    char_to_idx = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 
        'E': 5, 'F': 6, 'G': 7, 'H': 8
    }
    idx_to_char = {v: k for k, v in char_to_idx.items()}
    convert = lambda x: idx_to_char[x[0] + 1] + ' ' + str(x[1] + 1)

    # 이동할 네 가지 방향 정의 (왼위, 왼아, 오위, 오아)
    dx = [-1, -1, 1, 1]
    dy = [1, -1, 1, -1]

    r1, c1 = char_to_idx[xy_info[0]] - 1, int(xy_info[1]) - 1
    r2, c2 = char_to_idx[xy_info[2]] - 1, int(xy_info[3]) - 1

    visited = [[0] * 8 for _ in range(8)]
    visited[r1][c1] = 1  # 처음 위치
    queue = deque([((r1, c1), 0, convert([r1, c1]))])  # xy, cnt, path
    result = 'Impossible'  # 목적지에 갈 수 없다면 Impossible 반환

    while queue:
        xy, cnt, path = queue.popleft()
        
        # 목적지 도착
        if xy[0] == r2 and xy[1] == c2:
            result = str(cnt) + ' ' + path
            break

        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = xy[0]
            ny = xy[1]
            # 같은 방향, 여러칸 이동 탐색
            while True:  
                nx = nx + dx[i]
                ny = ny + dy[i]
                # 체스판을 벗어난 경우 무시 (1 ~ 8) x (1 ~ 8)
                if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                    break
                # 처음 방문한 곳이면
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append(((nx, ny), cnt + 1, path + ' ' + convert([nx, ny])))
    
    return result



if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        xy_info = input().split()
        print(bfs(xy_info))
        

    