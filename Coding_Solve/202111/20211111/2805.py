import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    height = list(map(int, input().split()))

    start = 1
    end = max(height)

    while start <= end:
        get_tree = 0
        mid = (start + end) // 2

        for h in height:
            if h - mid < 0:
                continue
            else:
                get_tree += (h - mid)

        if get_tree >= M:
            start = mid + 1
        else:
            end = mid - 1

    print(end)


if __name__ == '__main__':
    solution()
