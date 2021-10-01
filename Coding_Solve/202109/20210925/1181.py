import sys
input = sys.stdin.readline


def solution():
    _list.sort(key=lambda x: (len(x), x))
    for s in _list:
        print(s)

if __name__ == "__main__":
    N = int(input())
    _list = list(set([input().strip() for _ in range(N)]))
    solution()
