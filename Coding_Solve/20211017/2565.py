import sys
input = sys.stdin.readline


def solution():
    # n : 전깃줄의 개수
    n = int(input())
    # A 라인을 기준으로 정렬
    AB = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])

    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if AB[i][1] > AB[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(n - max(dp))


if __name__ == '__main__':
    solution()