from collections import deque
from sys import stdin
input = stdin.readline

def get_remain_cheese(r, c, cheese_arr, remain_cheese_list):
    # 방문한 곳
    visited = [[False] * c for _ in range(r)]

    queue = deque()
    queue.append([0, 0])
    visited[0][0] = True
    cheese_num = 0
    while queue:
        row, col = queue.popleft()

        # 상,하,좌,우 탐색
        for D in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            # 탐색할 row, col
            nr = row + D[0]
            nc = col + D[1]
            # 만약 cheese_arr 안에 있고 방문한적이 없는 곳인 경우
            if 0 <= nr < r and 0 <= nc < c and not visited[nr][nc]:
                # 치즈가 없는 곳인 경우
                if cheese_arr[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append([nr, nc])
                # 치즈가 있는 곳인 경우
                elif cheese_arr[nr][nc] == 1:
                    cheese_arr[nr][nc] = 0
                    cheese_num += 1
                    visited[nr][nc] = True

    remain_cheese_list.append(cheese_num)
    return cheese_num, cheese_arr, remain_cheese_list
        

if __name__ == '__main__':
    # row, col
    r, c = map(int, input().split())
    # cheese 위치
    cheese_arr = [list(map(int, input().split())) for _ in range(r)]
    # 남아있는 치즈 개수 리스트
    remain_cheese_list = []

    # 치가 모두 녹은 시간
    all_melt_time = 0
    while True:
        remain_cheese, cheese_arr, remain_cheese_list = get_remain_cheese(r, c, cheese_arr, remain_cheese_list)
        if remain_cheese == 0:
            break    
        all_melt_time += 1

    print(all_melt_time)
    print(remain_cheese_list[-2])

    
