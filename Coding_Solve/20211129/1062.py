import sys
from itertools import combinations

input = sys.stdin.readline


def convert(x):
    return ord(x) - ord('a')

def convert_2(arr):
    result = 0
    for a in arr:
        result |= (1 << a)
    return result

def solution():
    N, K = map(int, input().split())
    s = set([convert(a) for a in list('acint')])
    base = 0
    for i in s:
        # |= or 연산자
        base |= (1 << i)  # i == 0 이진법 1 == 2, i == 3 이진법 100 == 8, i == 8 이진법 100000000 == 256
    arr = [set(map(convert, input().strip())) for _ in range(N)]
    arr_2 = [convert_2(a) for a in arr]

    candidates = set().union(*arr) - s

    answer = 0
    if K < 5:
        print(answer)
    else:
        if len(candidates) <= (K - 5):
            print(N)
        else:
            for c in combinations(candidates, K - 5):
                temp = base
                for i in c:
                    temp |= (1 << i)
                temp ^= (1 << 26) - 1
                answer = max(answer, sum(1 if (temp & a) == 0 else 0 for a in arr_2))

            print(answer)


if __name__ == '__main__':
    solution()