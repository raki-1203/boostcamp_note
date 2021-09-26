import sys
input = sys.stdin.readline


def solution():
    _list =  [abs(x - w), abs(y - h), abs(x - 0), abs(y - 0)]
    print(min(_list))

if __name__ == "__main__":
    x, y, w, h = map(int, input().split())
    solution()
