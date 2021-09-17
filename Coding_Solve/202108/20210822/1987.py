# from collections import deque
# from copy import deepcopy
# from sys import stdin
# input = stdin.readline

# def solution(r, c, board):
#     # 상, 하, 좌, 우 방향
#     D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#     alphabet = set(board[0][0])
    
#     queue = deque()
#     queue.append([0, 0, 1, alphabet])  # row, col, cnt, alphabet

#     cnt_set = set()
#     while queue:
#         row, col, cnt, alphabet = queue.popleft()
#         cnt_set.add(cnt)

#         for d in D:
#             nr = row + d[0]
#             nc = col + d[1]
#             if 0 <= nr < r and 0 <= nc < c:
#                 # 새로운 칸에서 본적 없는 알파벳을 만나면
#                 if board[nr][nc] not in alphabet:
#                     temp_alphabet = deepcopy(alphabet)
#                     temp_alphabet.add(board[nr][nc])
#                     queue.append([nr, nc, cnt + 1, temp_alphabet])
                
#     print(max(cnt_set))

# if __name__ == '__main__':
#     r, c = map(int, input().split())
#     board = [list(input().strip()) for _ in range(r)]
    
#     solution(r, c, board)


### 시간초과 나서 해결이 안됨

from collections import deque
from sys import stdin
input = stdin.readline

def DFS(x, y, count):
    global result
    result = max(result, count)

    # 상, 하, 좌, 우 방향
    D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for d in D:
        nx = x + d[0]
        ny = y + d[1]
        # 새로운 칸에서 본적 없는 알파벳을 만나면
        if 0 <= nx < r and 0 <= ny < c and alphabet[board[nx][ny]] == 0:
            # 알파벳 리스트에 추가
            alphabet[board[nx][ny]] = 1
            DFS(nx, ny, count + 1)
            # DFS 탐색 끝나고 알파벳 리스트에서 제거
            alphabet[board[nx][ny]] = 0
                
    
if __name__ == '__main__':
    r, c = map(int, input().split())
    board = [list(map(lambda x: ord(x) - 65, input().strip())) for _ in range(r)]
    alphabet = [0] * 26  # 알파벳 26글자
    
    result = 1
    alphabet[board[0][0]] = 1
    DFS(0, 0, 1)

    print(result)

    
