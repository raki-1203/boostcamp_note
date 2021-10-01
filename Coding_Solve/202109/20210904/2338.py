from sys import stdin
input = stdin.readline

# 긴자리 계산
# 백준 2338

def solution(A, B):
    print(A + B)
    print(A - B)
    print(A * B)

if __name__ == '__main__':
    A = int(input().strip())
    B = int(input().strip())

    solution(A, B)
