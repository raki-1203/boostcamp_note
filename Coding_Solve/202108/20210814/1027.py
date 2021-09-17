from collections import deque
from sys import stdin
input = stdin.readline

def solution(N, arr):
    # 기울기 구하는 함수
    slope = lambda A, B: (B[1] - A[1]) / (B[0] - A[0])

    max_cnt = 0
    for i in range(N):
        # i번째 건물 좌표
        A = (i, arr[i])

        # 오른쪽으로 가까운 건물부터 확인
        cur_slope = None
        right_cnt = 0
        for r in range(i + 1, N):
            # r번째 건물 좌표    
            B = (r, arr[r])
            # i번째 건물과 r번째 건물 기울기
            slope_right = slope(A, B)
            # 이전 기울기와 현재 기울기를 비교해서 현재기울기가 크면 보이므로
            if cur_slope is None or cur_slope < slope_right:
                cur_slope = slope_right
                right_cnt += 1

        # 왼쪽으로 가까운 건물부터 확인
        cur_slope = None
        left_cnt = 0
        for l in range(i - 1, -1, -1):
            # l번째 건물 좌표
            B = (l, arr[l])
            # i번째 건물과 l번째 건물 기울기
            slope_left = slope(A, B)
            # 이전 기울기와 현재 기울기를 비교해서 현재기울기가 작으면 보이므로
            if cur_slope is None or cur_slope > slope_left:
                cur_slope = slope_left
                left_cnt += 1

        cnt = right_cnt + left_cnt

        if max_cnt < cnt:
            max_cnt = cnt
    
    return max_cnt

    

        
if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    print(solution(N, arr))
