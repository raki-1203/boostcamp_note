import sys
input = sys.stdin.readline


def solution():
    n = int(input())
    num_list = [list(map(int, input().split())) for _ in range(n)]

    for i in range(1, n):
        for j in range(i + 1):
            # 맨 왼쪽인 경우 한칸 위의 맨 왼쪽 수를 더하면 됨
            if j == 0:
                num_list[i][j] = num_list[i][j] + num_list[i - 1][j]
            # 맨 오른쪽인 경우 한칸 위의 맨 오른쪽 수를 더하면 됨
            elif i == j:
                num_list[i][j] = num_list[i][j] + num_list[i - 1][j - 1]
            # 그 외의 경우 한칸 위의 같은 위치와 하나 작은 위치 중 큰 값을 더하면 됨
            else:
                num_list[i][j] = num_list[i][j] + max(num_list[i - 1][j], num_list[i - 1][j - 1])

    print(max(num_list[n - 1]))

if __name__ == '__main__':
    solution()
