import sys
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    # 미리 누적합 구해놓기
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = num_list[i - 1] + prefix_sum[i - 1]

    for _ in range(M):
        # j 번재 누적합에서 i-1 번째 누적합을 빼면 끝
        i, j = map(int, input().split())
        print(prefix_sum[j] - prefix_sum[i - 1])


if __name__ == "__main__":
    solution()
