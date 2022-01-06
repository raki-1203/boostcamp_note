import sys
input = sys.stdin.readline


def multiply(arr):
    ans = 1
    for n in arr:
        if n == 0:
            return 0
        ans *= n
    return ans


def solution():
    N = int(input())
    a_list = []
    b_list = []
    for _ in range(N):
        a, b = map(int, input().split())
        a_list.append(a)
        b_list.append(b)

    result_list = []

    # 부분집합의 총 갯수만큼 for 문 돌리기
    for i in range(1 << N):
        a_temp = []
        b_temp = []
        # 주어진 N 개의 리스트 확인하는 for 문
        for j in range(N):
            # i 는 찾으려는 부분집합 j 는 리스트의 인덱스 번호
            # 찾으려는 부분집합과 현재 인덱스 번호 사이의 교집합이 있다면
            if i & (1 << j):
                a_temp.append(a_list[j])
                b_temp.append(b_list[j])
        result_list.append(abs(multiply(a_temp) - sum(b_temp)))

    print(min(result_list[1:]))

if __name__ == '__main__':
    solution()