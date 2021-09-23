import sys
input = sys.stdin.readline


def solution(coin_list, K):
    # 동전 개수
    cnt = 0

    # 큰것부터 확인
    for c in coin_list[::-1]:
        # K 보다 동전이 작은 수면
        if K >= c:
            # 몫 만큼 동전을 사용하면 됨
            Q = K // c
            # 목표금액에서 뺴주고
            K -= c * Q
            # 동전 개수에 몫 만큼 더해줌
            cnt += Q
        # K 가 0 이 되면 빠져나옴
        if K == 0:
            break

    print(cnt)

if __name__ == "__main__":
    N, K = map(int, input().split())
    coin_list = [int(input()) for _ in range(N)]
    solution(coin_list, K)
