import sys
input = sys.stdin.readline


def solution():
    print(A + B)


if __name__ == "__main__":
    while True:
        try:
            _input = input()
            A, B = map(int, _input.split())
            solution()
        except Exception as e:
            break
