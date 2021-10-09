import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    RGB_price = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N):
        # Red
        RGB_price[i][0] = min(RGB_price[i - 1][1], RGB_price[i - 1][2]) + RGB_price[i][0]
        # Green
        RGB_price[i][1] = min(RGB_price[i - 1][0], RGB_price[i - 1][2]) + RGB_price[i][1]
        # Blue
        RGB_price[i][2] = min(RGB_price[i - 1][0], RGB_price[i - 1][1]) + RGB_price[i][2]
    print(min(RGB_price[N - 1]))


if __name__ == '__main__':
    solution()
