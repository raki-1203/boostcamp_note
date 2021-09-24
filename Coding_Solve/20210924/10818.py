import sys
input = sys.stdin.readline


def solution():
    print(min(_list), max(_list))


if __name__ == "__main__":
    N = int(input())
    _list = list(map(int, input().split()))
    solution()
