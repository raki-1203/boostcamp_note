from collections import deque
from sys import stdin
input = stdin.readline

def solution(command_list, N):
    if len(command_list) == 3:
        command, i, x = command_list
    else:
        command, i = command_list
        
    if command == 1:
        if train_list[i - 1][x - 1] == 1:
            return
        else:
            train_list[i - 1][x - 1] = 1
    elif command == 2:
        if train_list[i - 1][x - 1] == 0:
            return
        else:
            train_list[i - 1][x - 1] = 0
    elif command == 3:
        train_list[i - 1].pop()
        train_list[i - 1].insert(0, 0)
    elif command == 4:
        train_list[i - 1].pop(0)
        train_list[i - 1].append(0)
        
    
if __name__ == '__main__':
    N, M = map(int, input().split())
    # 기차 좌석 리스트
    train_list = [[0] * 20 for _ in range(N)]
    for _ in range(M):
        command_list = list(map(int, input().split()))
        solution(command_list, N)
    # 은하수 건넌 기차
    galaxy_list = []
    for train in train_list:
        # 은하수 건넌 기차에 기차랑 똑같은 형태가 없으면
        if train not in galaxy_list:
            galaxy_list.append(train)

    print(len(galaxy_list))
       
