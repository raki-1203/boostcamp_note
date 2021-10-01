import sys
input = sys.stdin.readline


def solution():
    if list(string) == list(string)[::-1]:
        print('yes')
    else:
        print('no')

if __name__ == "__main__":
    while True:
        string = input().strip()
        if string == '0':
            break
        solution()
