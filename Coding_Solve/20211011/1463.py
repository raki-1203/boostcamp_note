import sys
input = sys.stdin.readline


def solution():
    N = int(input())

    dp = [0, 0, 1, 1]

    # N 이 3 이하면 그냥 출력
    if N <= 3:
        print(dp[N])
        return

    # N 이 4 이상이면
    for i in range(4, N + 1):
        # -1 작업 할 경우 계산 수가 1 증가하므로 직전 계산수에 1 더함
        min_num = dp[i - 1] + 1

        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            # 3으로 나눴을 때 나오는 수의 계산 수에 +1
            temp = dp[i // 3] + 1
            # -1 작업했을 때와 최소 계산수 비교
            min_num = min(min_num, temp)
        # 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            # 2로 나눴을 때 나오는 수의 계산 수에 +1
            temp = dp[i // 2] + 1
            # 위에서 정해진 최소 계산수 비교
            min_num = min(min_num, temp)

        # dp list 에 추가
        dp.append(min_num)

    # 마지막 dp 값 추가
    print(dp[N])


if __name__ == '__main__':
    solution()