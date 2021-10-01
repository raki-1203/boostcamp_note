import sys
input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))

    # 미리 누적합 구해놓기
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = num_list[i - 1] + prefix_sum[i - 1]

    K_sum_list = []
    for i in range(K, N + 1):
        # j 번재 누적합에서 i-K 번째 누적합을 빼면 끝
        K_sum_list.append(prefix_sum[i] - prefix_sum[i - K])
    print(max(K_sum_list))


if __name__ == "__main__":
    solution()
