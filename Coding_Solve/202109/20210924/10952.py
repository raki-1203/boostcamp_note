import sys
input = sys.stdin.readline


def solution():
    print(A + B)


if __name__ == "__main__":
    while True:
        _input = input()
        A, B = map(int, _input.split())
        if A == 0 and B == 0:
            break
        solution()
