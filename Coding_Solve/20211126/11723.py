import sys

input = sys.stdin.readline


def solution():
    M = int(input())
    S = set()
    for _ in range(M):
        string = input().strip()
        if string in ('all', 'empty'):
            func = string

            if func == 'all':
                S = set(list(range(1, 21)))
            elif func == 'empty':
                S = set()
        else:
            func, x = string.split()
            x = int(x)

            if func == 'add':
                S.add(x)
            elif func == 'remove':
                S.discard(x)
            elif func == 'check':
                if x in S:
                    print(1)
                else:
                    print(0)
            elif func == 'toggle':
                if x in S:
                    S.discard(x)
                else:
                    S.add(x)


if __name__ == '__main__':
    solution()
