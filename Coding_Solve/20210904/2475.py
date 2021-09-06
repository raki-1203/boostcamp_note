from sys import stdin
input = stdin.readline

# 검증수
# 백준 2475

def solution(num_list):
    print(sum(num_list) % 10)


if __name__ == '__main__':
    num_list = list(map(lambda x: int(x)**2, input().split()))

    solution(num_list)
