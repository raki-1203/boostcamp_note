import sys
input = sys.stdin.readline

def solution():
    melody_num = (I - 1) * A + 1
    print(melody_num)


if __name__ == '__main__':
    A, I = map(int, input().split())
    solution()
