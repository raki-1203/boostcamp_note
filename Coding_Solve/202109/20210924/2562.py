import sys
input = sys.stdin.readline


def solution():
    max_num = 0
    max_idx = -1
    for i, num in enumerate(_list, 1):
        if max_num < num:
            max_num = num
            max_idx = i

    print(max_num)
    print(max_idx)


if __name__ == "__main__":
    _list = [int(input()) for _ in range(9)]
    solution()
