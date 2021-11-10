import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    num_card = sorted(list(map(int, input().split())))
    num_card_dict = {}
    for num in num_card:
        if num in num_card_dict:
            num_card_dict[num] += 1
        else:
            num_card_dict[num] = 1

    M = int(input())
    check_num = list(map(int, input().split()))

    result = []
    for num in check_num:
        result.append(num_card_dict.get(num, 0))

    print(*result)



if __name__ == '__main__':
    solution()
