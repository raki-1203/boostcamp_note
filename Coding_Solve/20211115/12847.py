import sys
input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    T = list(map(int, input().split()))

    # 누적합 리스트
    cumsum = [0]
    for t in T:
        cumsum.append(cumsum[len(cumsum) - 1] + t)

    # 누적합리스트에서 n 일 동안 연속해서 일해야 하므로 n 일 전꺼를 빼면 받을 수 있는 금액이 되니 그중 제일 큰 값을 선택
    max_cumsum = 0
    for i in range(m, n + 1):
        max_cumsum = max(max_cumsum, cumsum[i] - cumsum[i - m])

    print(max_cumsum)


if __name__ == '__main__':
    solution()