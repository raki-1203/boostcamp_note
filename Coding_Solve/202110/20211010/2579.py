import sys
input = sys.stdin.readline


def solution():
    n = int(input())
    stair = [0] + [int(input()) for _ in range(n)]

    if n == 1:
        print(stair[1])
    else:
        dp = [0] * (n + 1)
        dp[1] = stair[1]
        dp[2] = stair[1] + stair[2]

        for i in range(3, n + 1):
            dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])

        print(dp[n])

if __name__ == '__main__':
    solution()
