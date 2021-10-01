from sys import stdin
input = stdin.readline

# 16진수
# 백준 1550

def solution(num_by_16):
    print(int(num_by_16, 16))

if __name__ == '__main__':
    num_by_16 = input().strip()

    solution(num_by_16)
