from collections import deque
from sys import stdin
input = stdin.readline



def solution():
    horse_direction = [(1, 2), (-1, 2), (-2, 1), (2, 1), (-1, -2), (1, -2), (-2, -1), (2, -1)]
    monkey_direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = deque()
    queue.append((0, 0, K))  # x, y, K
    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]

    while queue:
        x, y, z = queue.popleft()

        # 도착지에 도착한 경우
        if x == H - 1 and y == W - 1:
            return visited[x][y][z]

        # 말처럼 K번을 움직이지 않은 경우
        if z > 0:
            for D in horse_direction:
                nx = x + D[0]
                ny = y + D[1]
                # 주어진 보드판 위에서 움직이고 방문한적 없고 장애물이 없으면
                if 0 <= nx < H and 0 <= ny < W and visited[nx][ny][z - 1] == 0 and board[nx][ny] != 1:
                    # K 가 -1 만큼 줄어들고 이동한 칸에 움직인 횟수 +1
                    visited[nx][ny][z - 1] = visited[x][y][z] + 1
                    queue.append((nx, ny, z - 1))

        for D in monkey_direction:
            nx = x + D[0]
            ny = y + D[1]

            # 주어진 보드판 위에서 움직이고 방문한적 없고 장애물이 없으면
            if 0 <= nx < H and 0 <= ny < W and visited[nx][ny][z] == 0 and board[nx][ny] != 1:
                # K 값은 말이 이동하는 것처럼 움직이지 않으므로 줄지 않고 이동한 칸에 움직인 횟수 +1 해준다.
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))

    return -1


if __name__ == '__main__':
    K = int(input())
    W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]

    print(solution())