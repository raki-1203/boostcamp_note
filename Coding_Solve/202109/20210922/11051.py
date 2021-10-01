import sys
input = sys.stdin.readline


def solution():
    # 이윤
    profit = 0
    # 마지막 가격을 최고 가격이라고 가정
    max_price = price[-1]
    for i in range(N - 2, -1, -1):
        # 만약 max_price 보다 가격이 크면 max_price 를 변경
        if price[i] > max_price:
            max_price = price[i]
        # max_price 보다 가격이 작으면 이윤에 더해줌
        else:
            profit += max_price - price[i]

    print(profit)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        price = list(map(int, input().split()))
        solution()
