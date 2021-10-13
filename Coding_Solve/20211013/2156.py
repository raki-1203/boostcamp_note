import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    grape = [0] + [int(input()) for _ in range(n)]

    if n == 1:
        print(grape[1])
    else:
        dp = [0] * (n + 1)
        dp[1] = grape[1]
        dp[2] = grape[1] + grape[2]

        for i in range(3, n + 1):
            # 계단오르기와 다르게 현재 계단을 굳이 안밟아도 됨
            # 전전전 포도주스 + 전 포도주스 + 현재 포도주스 vs 전전 포도주스 + 현재 포도주스 vs 이전 포도주스 의 max 값 비교
            dp[i] = max(dp[i - 3] + grape[i - 1] + grape[i], dp[i - 2] + grape[i], dp[i - 1])

        print(dp[n])


if __name__ == '__main__':
    solution()