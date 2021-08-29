from sys import stdin
input = stdin.readline


def solution():
    pass

if __name__ == '__main__':
    # N: 연꽃 개수, M: 통나무 개수
    N, M = map(int, input().split())

    # 음식: 1, 취미: 2, 가족: 3, 철학: 4 흥미도
    interest_arr = [list(map(int, input().split())) for _ in range(N)]
    favorite_lotus = [list(map(int, input().split())) for _ in range(N)]
    ABT_arr = [list(map(int, input().split())) for _ in range(M)]

    solution()
