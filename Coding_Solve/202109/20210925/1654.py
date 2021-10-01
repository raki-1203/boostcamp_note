import sys
input = sys.stdin.readline


def solution():
    # 만약 최소값의 중앙값의 길이로 N 개의 랜선을 만들 수 있으면 그 위의 값의 중앙값을 찾고
    # 최소값의 중앙값의 길이로 N 개의 랜선을 만들 수 없으면 그 값보다 작은 값의 중앙값을 찾음
    start = 1
    end = max(_list)

    result = 0
    while start <= end:
        median = (start + end) // 2
        cnt = 0
        for l in _list:
            cnt += l // median

        if cnt >= N:
            start = median + 1
            result = median
        else:
            end = median - 1

    print(result)


if __name__ == "__main__":
    K, N = map(int, input().split())
    _list = [int(input()) for _ in range(K)]
    solution()
