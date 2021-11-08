import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    A = list(map(int, input().split()))

    dp = [1] * N

    # A 수열에서 특정 위치에서 자기 보다 앞에서의 수가 작은 애들을 모두 count 해주면 그 위치까지의 증가하는 수열의 길이를 구할 수 있음
    for i in range(N):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


if __name__ == '__main__':
    solution()