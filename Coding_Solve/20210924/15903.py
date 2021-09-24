import sys
input = sys.stdin.readline


def solution(num_list):
    # m 번 카드합치기
    for _ in range(m):
        # 오름차순 정렬
        num_list.sort()
        # 가장 작은 2개 수의 합
        s = sum(num_list[:2])
        # num_list 에 작은수 2개 빼고 합쳐진 숫자 2개 추가
        num_list = num_list[2:] + [s] * 2

    print(sum(num_list))


if __name__ == "__main__":
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))
    solution(num_list)
