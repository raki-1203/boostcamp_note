import sys
input = sys.stdin.readline


def solution():
    N = int(input().strip())
    k = int(input().strip())

    start = 1
    end = k  # k 번째 수는 k 를 넘을 수 없다.

    answer = None

    while start <= end:
        mid = (start + end) // 2

        temp = 0
        for i in range(1, N + 1):
            temp += min(mid // i, N)  # mid 이하의 i 의 배수 개수 or 최대 N

        if temp >= k:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    print(answer)


if __name__ == '__main__':
    solution()