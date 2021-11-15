import sys

input = sys.stdin.readline


def find_low(LIS, num):
    start = 0
    end = len(LIS) - 1

    ret = 1000000

    while start <= end:
        mid = (start + end) // 2
        if LIS[mid] >= num:
            if ret > mid:
                ret = mid
            end = mid - 1
        else:
            start = mid + 1

    return ret


def solution():
    N = int(input())
    A = list(map(int, input().split()))

    # 가장 긴 증가하는 부분 수열
    LIS = [A[0]]

    for i in range(1, N):
        if LIS[len(LIS) - 1] < A[i]:
            LIS.append(A[i])
        else:
            LIS[find_low(LIS, A[i])] = A[i]

    print(len(LIS))


if __name__ == '__main__':
    solution()
