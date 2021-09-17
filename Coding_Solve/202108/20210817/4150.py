from collections import deque
from sys import stdin

input = stdin.readline

def solution(N):
    # 0 ~ 2번 피보나치 결과
    arr = [0, 1, 1]
    # 3번 부터 for 문 돌려서 arr 에 쌓아 놓기
    for i in range(3, N + 1):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[N]

        
if __name__ == '__main__':
    N = int(input())
    print(solution(N))
