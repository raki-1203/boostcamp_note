import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    A = list(map(int, input().split()))

    # 증가하는 수열부분
    increase_dp = [1] * N
    # 감소하는 수열 부분
    decrease_dp = [1] * N

    for i in range(N):
        for j in range(i):
            if A[i] > A[j]:
                increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)

    for i in range(N - 1, -1, -1):
        for j in range(N - 1, i, -1):
            if A[i] > A[j]:
                decrease_dp[i] = max(decrease_dp[i], decrease_dp[j] + 1)

    dp = [0] * N
    # 증가와 감소를 합치고 -1 해줌
    for i in range(N):
        dp[i] = increase_dp[i] + decrease_dp[i] - 1

    print(max(dp))


if __name__ == '__main__':
    solution()