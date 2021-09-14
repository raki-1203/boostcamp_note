import sys
input = sys.stdin.readline

def factorial(n):
    num = 1
    for i in range(2, n + 1):
        num *= i
    return num

def solution():
    # M 개의 site 중 N 개를 고르고 다리가 겹치면 안되니까 줄을 세울 수 있는 방법이 1개 밖에 없음
    # 순서에 상관없이 M 개의 site 중 N 개를 고르는 방법은 조합을 사용하면 됨
    # 조합 공식 M!/(N!)(M-N)!
    result = factorial(M) / (factorial(N) * factorial(M - N))
    print(int(result))

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        solution()