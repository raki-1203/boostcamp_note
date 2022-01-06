import sys
input = sys.stdin.readline


def solution():
    n = int(input())  # 기관차가 끌고 가던 객차의 수
    people = list(map(int, input().split()))
    m = int(input())  # 소형 기관차가 최대로 끌 수 있는 객차의 수

    cumsum = [0]
    value = 0
    for p in people:
        value += p
        cumsum.append(value)

    dp = [[0] * (n + 1) for _ in range(4)]

    # 점화식을 이용해 최댓값 탐색
    for i in range(1, 4):
        for j in range(i * m, n + 1):
            # n = 1일 때 선택한 객차가 없으므로
            # 전에 계산한 구간합과 현재 계산하는 구간합 중 최댓값을 계산해 갱신해준다.
            if i == 1:
                dp[i][j] = max(dp[i][j-1], cumsum[j] - cumsum[j-m])
            # 점화식
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-m] + cumsum[j] - cumsum[j - m])

    print(dp[3][n])



if __name__ == '__main__':
    solution()