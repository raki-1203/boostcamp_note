from collections import deque
from sys import stdin
input = stdin.readline

def solution(H, W, height_list):
    water = 0
    for i in range(1, W - 1):
        # 현재 위치보다 왼쪽 블록중에 가장 큰 높이를 찾는다.
        left_height = height_list[i]
        for j in range(i - 1, -1, -1):
            if left_height < height_list[j]:
                left_height = height_list[j]

        # 현재 위치보다 오른쪽 블록중에 가장 큰 높이를 찾는다.
        right_height = height_list[i]
        for j in range(i + 1, W):
            if right_height < height_list[j]:
                right_height = height_list[j]

        # 왼쪽, 오른쪽 높이 중 작은 높이에서 현재 높이를 뺸 값을 더한다.
        final_height = min(left_height, right_height)
        water += final_height - height_list[i]
        
    print(water)
        
        
    
if __name__ == '__main__':
    # H : 세로 길이
    # W : 가로 길이
    H, W = map(int, input().split())
    # 블록이 쌓인 높이 리스트
    height_list = list(map(int, input().split()))
    solution(H, W, height_list)
       
