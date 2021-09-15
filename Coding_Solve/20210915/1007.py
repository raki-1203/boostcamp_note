from itertools import combinations
import math
import sys
input = sys.stdin.readline


def solution():
    min_length = math.inf

    comb_list = list(combinations(P, N//2))
    for vector_list in comb_list[:len(comb_list) // 2]:
        # 더해야하는 좌표 총합
        x1_total = 0
        y1_total = 0
        for x1, y1 in vector_list:
            x1_total += x1
            y1_total += y1

        # 빼야하는 좌표 총합(= 모든 좌표들의 총합 - 더해야하는 좌표 총합)
        x2_total = x_total - x1_total
        y2_total = y_total - y1_total

        # 벡터의 길이
        length = math.sqrt((x1_total - x2_total)**2 + (y1_total - y2_total)**2)
        min_length = min(length, min_length)

    print(min_length)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())

        # 모든 좌표들의 총합
        x_total = 0
        y_total = 0
        P = []
        for _ in range(N):
            x, y = map(int, input().split())
            x_total += x
            y_total += y
            P.append([x, y])
        solution()
