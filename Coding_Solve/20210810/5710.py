from sys import stdin
input = stdin.readline

def get_total_Wh_from_bill(A):
    # 사용량에 따른 기준 요금
    pay_list = [100 * 2, 100 * 2 + 9900 * 3, 100 * 2 + 9900 * 3 + 990000 * 5]
    if A <= pay_list[0]:
        total_Wh = A // 2
    elif A <= pay_list[1]:
        total_Wh = 100 + (A - pay_list[0]) // 3
    elif A <= pay_list[2]:
        total_Wh = 10000 + (A - pay_list[1]) // 5
    else:
        total_Wh = 1000000 + (A - pay_list[2]) // 7

    return total_Wh

def get_bill_from_Wh(Wh):
    # 사용 기준량
    limit_list = [100, 10000, 1000000]
    if Wh <= limit_list[0]:
        bill = Wh * 2
    elif Wh <= limit_list[1]:
        bill = 100 * 2 + (Wh - limit_list[0]) * 3
    elif Wh <= limit_list[2]:
        bill = 100 * 2 + 9900 * 3 + (Wh - limit_list[1]) * 5
    else:
        bill = 100 * 2 + 9900 * 3 + 990000 * 5 + (Wh -limit_list[2]) * 7

    return bill

def solution(A, B):
    total_Wh = get_total_Wh_from_bill(A)

    start = 1
    end = total_Wh
    while True:
        # x 상근이
        x = (start + end) // 2
        # y 이웃
        y = total_Wh - x

        # 이웃 - 상근이 요금
        diff_xy = get_bill_from_Wh(y) - get_bill_from_Wh(x)

        # 차이가 B와 같으면 그 때의 상근이의 요금 출력
        if diff_xy == B:
            return get_bill_from_Wh(x)
            
        # 차이가 B 보다 큰 것은 x의 사용량이 늘어나야함
        if diff_xy > B:
            start = x + 1
        # 차이가 B 보다 작으면 x의 사용량이 줄어들어야함
        else:
            end = x - 1


if __name__ == '__main__':
    while True:
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            break
        print(solution(A, B))
