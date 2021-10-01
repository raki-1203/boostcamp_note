import sys
input = sys.stdin.readline


def solution():
    m = M - 45
    if m < 0:
        m = 60 + m
        h = H - 1
        if h < 0:
            h = 23
    else:
        h = H

    print(h, m)

if __name__ == "__main__":
    H, M = map(int, input().split())
    solution()
