from sys import stdin
input = stdin.readline

def solution(N, arr):
    # 순서를 기록할 리스트
    order_list = [0] * N

    for i in range(N):
        # 키가 i + 1 인 사람의 왼쪽에 자기보다 큰 사람의 수
        num = arr[i]
        # 키가 i + 1 인 사람의 j + 1 번쨰 위치의 있을 경우 왼쪽에 자기보다 큰 사람의 수
        cnt = 0
        for j in range(N):
            # 만약 기억하는 숫자와 cnt가 같고 그 자리에 미리 선 사람이 없다면
            if num == cnt and order_list[j] == 0:
                order_list[j] = i + 1
                break
            # 그 자리에 미리 선 사람이 없다면
            if order_list[j] == 0:
                cnt += 1
        
    print(*order_list)
        


if __name__ == "__main__":
    N = int(input())
    arr = [int(n) for n in input().strip().split()]
    solution(N, arr)
    