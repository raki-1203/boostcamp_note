import sys
input = sys.stdin.readline


def solution():
    print(len(set([num % 42 for num in _list])))

if __name__ == "__main__":
    _list = [int(input()) for _ in range(10)]
    solution()
