import sys
input = sys.stdin.readline


def solution():
    cnt = 0
    for num in range(666, 999999999):
        if '666' in str(num):
            cnt += 1
        if N == cnt:
            print(num)
            break


if __name__ == "__main__":
    N = int(input())
    solution()
