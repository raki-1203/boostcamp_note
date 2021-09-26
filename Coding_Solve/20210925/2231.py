import sys
input = sys.stdin.readline


def solution():
    # M 의 분해합이 N 인 경우, M 을 N 의 생성자라 한다.
    # N 의 가장 작은 생성자를 구하려면 분해합 N 을 가지는 가장 작은 수를 구해야 함
    # 분해합은 자기 자신을 더해야 하므로 N 보다 작거나 같을 수 밖에 없음
    for num in range(1, N + 1):
        _list = list(map(int, [str(num)] + [i for i in str(num)]))
        if sum(_list) == N:
            print(num)
            return

    print(0)


if __name__ == "__main__":
    N = int(input())
    solution()
