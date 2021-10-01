from sys import stdin
input = stdin.readline

# 파티가 끝나고 난 뒤
# 백준 2845

def solution():
    real_people_num = L * P
    diff_num_list = [num - real_people_num for num in news_info]
    print(*diff_num_list)


if __name__ == '__main__':
    L, P = map(int, input().split())
    news_info = list(map(int, input().split()))

    solution()
