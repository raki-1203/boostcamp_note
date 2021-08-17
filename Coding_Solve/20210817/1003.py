from collections import deque
from sys import stdin

input = stdin.readline

def solution(num):
    arr = [(1, 0), (0, 1)]
    for i in range(2, num + 1):
        arr.append((arr[i - 1][0] + arr[i - 2][0], arr[i - 1][1] + arr[i - 2][1]))
    print(*arr[num])

        
if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        num = int(input())
        solution(num)

