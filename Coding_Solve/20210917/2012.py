import sys
input = sys.stdin.readline


def solution():
    # 순위를 전부 집합에 담기
    best_rank = set(range(1, N+1))
    # 예상순위가 겹치는 남는 예상순위 담는 배열
    left_rank = []
    for pr in predict_rank:
        if pr in best_rank:
            best_rank.remove(pr)
        else:
            left_rank.append(pr)

    # 비어있는 순위 리스트로 변경하고 정렬
    best_left_rank = sorted(list(best_rank))
    # 예상순위가 겹치는 남는 예상순위 정렬
    left_rank = sorted(left_rank)

    result = 0
    # 비어있는 순위와 남은 사람의 예상 순위의 절대값 계산해서 전부 더하기
    for lr, blr, in zip(left_rank, best_left_rank):
        result += abs(lr - blr)

    print(result)


if __name__ == "__main__":
    N = int(input())
    predict_rank = [int(input()) for _ in range(N)]
    solution()
