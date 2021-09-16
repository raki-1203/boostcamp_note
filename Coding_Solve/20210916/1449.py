import sys
input = sys.stdin.readline


def solution():
    # 테이프를 가장 왼쪽의 위치에서 한개 붙이고 시작!
    num = 1
    # 테이프 한장의 끝 부분은 이렇게 계산 가능 -> 물새는 위치 + 테이프 길이 - 0.5
    end_tape = place.pop(0) + L - 0.5

    for p in place:
        # 테이프 끝 부분보다 위치가 안쪽인 경우는 패스
        if end_tape > p:
            continue
        # 그렇지 않은 경우는 tape 개수 추가해주고 새로운 테이프 한장의 끝 부분 업데이트
        else:
            num += 1
            end_tape = p + L - 0.5

    print(num)


if __name__ == "__main__":
    N, L = map(int, input().split())
    # 혹시 몰라서 미리 정렬
    place = sorted(list(map(int, input().split())))
    solution()
