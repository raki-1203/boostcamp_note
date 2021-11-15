import math
import sys
input = sys.stdin.readline


def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X = list(map(int, input().split()))

        cumsum = [0]
        for x in X:
            cumsum.append(cumsum[len(cumsum)-1] + x)

        max_cumsum = -math.inf
        for i in range(len(cumsum)):
            for j in range(i + 1, len(cumsum)):
                max_cumsum = max(max_cumsum, cumsum[j] - cumsum[i])

        print(max_cumsum)





if __name__ == '__main__':
    solution()