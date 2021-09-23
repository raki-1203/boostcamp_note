import sys
input = sys.stdin.readline


def solution():
    if C - B == 0 or A / (C - B) <= 0:
        print(-1)
    else:
        print(int(A / (C - B) + 1))


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    solution()
