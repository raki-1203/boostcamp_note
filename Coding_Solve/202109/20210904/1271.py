from sys import stdin
input = stdin.readline

# 엄청난 부자 2
# 백준 1271

def solution(n, m):
    share, remainder = divmod(n, m)
    print(share)
    print(remainder)

if __name__ == '__main__':
    n, m = map(int, input().split())

    solution(n, m)
