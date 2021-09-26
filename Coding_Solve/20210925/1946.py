import sys
input = sys.stdin.readline


def solution(_score):
    # 서류심사 순위로 정렬
    _score.sort(key=lambda x: x[0])
    # 1등은 무조건 합격
    cnt = 1
    # 1등 면접 순위
    rank = _score[0][1]

    # 서류심사 순위 2등부터
    for i in range(1, N):
        # rank 보다 순위가 낮으면 합격
        if rank > _score[i][1]:
            cnt += 1
            # 합격한 rank 업데이트
            rank = _score[i][1]

    print(cnt)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        _score = [list(map(int, input().split())) for _ in range(N)]
        solution(_score)
