from sys import stdin
input = stdin.readline


def solution(N, num_list):
    # increase
    increase_max_cnt = 1
    cnt = 1
    for i in range(N - 1):
        if num_list[i] <= num_list[i + 1]:
            cnt += 1
            increase_max_cnt = max(increase_max_cnt, cnt)
        else:
            cnt = 1

    reverse_num_list = num_list[::-1]
    # decrease
    decrease_max_cnt = 0
    cnt = 1
    for i in range(N - 1):
        if reverse_num_list[i] <= reverse_num_list[i + 1]:
            cnt += 1
            decrease_max_cnt = max(decrease_max_cnt, cnt)
        else:
            cnt = 1

    print(max(increase_max_cnt, decrease_max_cnt))



if __name__ == '__main__':
    # N: 연꽃 개수, M: 통나무 개수
    N = int(input())

    # 수열
    num_list = list(map(int, input().split()))

    solution(N, num_list)
