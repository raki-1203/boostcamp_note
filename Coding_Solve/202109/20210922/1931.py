import sys
input = sys.stdin.readline


def solution():
    # 회의 개수
    cnt = 1
    # 회의 끝나는 시간으로 정렬
    # 이 때 질문검색에서 반례를 좀 찾아내서 해결할 수 있었음
    # 문제는 start=5, end=7 인 경우와 start=7, end=7 인 경우 7, 7 인 경우가 먼저 나와버리면 하나 빠져버리게 됨
    # 그래서 정렬을 할 때, end 를 기준으로 정렬하고 end 가 같은 경우는 start 로 한번 더 정렬
    start_end_time.sort(key=lambda x: (x[1], x[0]))

    # 이전 회의 끝나는 시간
    ex_end = start_end_time[0][1]
    for start, end in start_end_time[1:]:
        # 이전 회의 끝나는 시간보다 회의 시작 시간이 같거나 느리면
        if start >= ex_end:
            ex_end = end
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    N = int(input())
    start_end_time = [list(map(int, input().split())) for _ in range(N)]
    solution()
