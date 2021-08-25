from itertools import combinations
from sys import stdin
input = stdin.readline

def solution(N, SB_arr):
    # 부분집합 리스트
    subset_list = [[]]
    for i in range(N):
        size = len(subset_list)
        for j in range(size):
            subset_list.append(subset_list[j] + [i])

    # 공집합 제거
    subset_list.pop(0)

    # 쓴맛과 신맛의 차이 최소값
    min_SB_diff = 1000000000
    for subset in subset_list:
        total_S = 1  # 신맛
        total_B = 0  # 쓴맛
        for idx in subset:
            S, B = SB_arr[idx]
            total_S *= S
            total_B += B
        
        SB_diff = abs(total_S - total_B)
        if min_SB_diff > SB_diff:
            min_SB_diff = SB_diff

    print(min_SB_diff)
        
        
    
if __name__ == '__main__':
    # N : 재료의 개수
    N = int(input())
    # 신맛: S, 쓴맛: B 배열
    SB_arr = [list(map(int, input().split())) for _ in range(N)]
    solution(N, SB_arr)
       
