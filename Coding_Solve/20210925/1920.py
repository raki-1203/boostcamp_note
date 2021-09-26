import sys
input = sys.stdin.readline


def solution(num):
    if num in A_list:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    N = int(input())
    A_list = set(map(int, input().split()))
    M = int(input())
    _list = list(map(int, input().split()))
    for num in _list:
        solution(num)
