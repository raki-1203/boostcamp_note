import sys
input = sys.stdin.readline


def solution():
    N, H = map(int, input().split())
    # 높이가 i 인 석순, 높이가 H - i + 1 인 종유석
    top = [0] * (H + 1)  # 종유석
    bottom = [0] * (H + 1)  # 석순

    min_count = N  # 파괴해야 하는 장애물의 최소값
    range_count = 0  # 최소값이 나타나는 구간의 수

    length = [int(input()) for _ in range(N)]
    for i, l in enumerate(length):
        if i % 2 == 0:
            bottom[H - l + 1] += 1
        else:
            top[l] += 1

    # 각 높이로 잘랐을 때 생기는 조각의 개수
    # i 줄을 잘랐을 때 석순은 높이가 i 인 석순의 개수와 i + 1 이상의 석순의 개수
    for i in range(H - 1, 0, -1):
        top[i] += top[i + 1]

    # i 줄을 잘랐을 때 종유석의 위치가 i 인 석순의 개수와 i - 1 이하에 위치한 종유석의 개수
    for i in range(1, H + 1):
        bottom[i] += bottom[i - 1]

    total = [0] * (H + 1)
    for i in range(1, H + 1):
        total[i] = top[i] + bottom[i]

    # 0번 인덱스 제외
    res = total[1:]
    v = min(res)
    print(v, res.count(v))


if __name__ == '__main__':
    solution()
