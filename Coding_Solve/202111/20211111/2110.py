import sys

input = sys.stdin.readline


def solution():
    N, C = map(int, input().split())
    x_list = sorted([int(input().strip()) for _ in range(N)])

    start = 1  # 최소거리
    end = x_list[-1] - x_list[0]  # 최대거리

    while start <= end:
        mid = (start + end) // 2
        current = x_list[0]
        cnt = 1

        for x in x_list[1:]:
            if x >= current + mid:
                cnt += 1
                current = x

        if cnt >= C:
            start = mid + 1
        else:
            end = mid - 1

    print(end)


if __name__ == '__main__':
    solution()
