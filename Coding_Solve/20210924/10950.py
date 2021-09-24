import sys
input = sys.stdin.readline


def solution():
    print(A + B)


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        solution()
