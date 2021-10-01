import heapq
import sys
input = sys.stdin.readline


def solution():
    # 처음 도시에서는 무조건 기름을 넣어야 하므로 미리 계산
    total_price = price[0] * distance[0]

    heap = []
    heapq.heappush(heap, price[0])

    # 두번째 도로 길이와 두번째 도시 기름 가격부터 마지막 이전 도시의 기름 가격까지만
    for d, p in zip(distance[1:], price[1:-1]):
        # heap 에 다음 도시의 가격을 넣고 거리만큼 가장 싼 가격으로 계속 더해나가면 됨
        heapq.heappush(heap, p)
        total_price += heap[0] * d

    print(total_price)

if __name__ == "__main__":
    N = int(input())
    distance = list(map(int, input().split()))
    price = list(map(int, input().split()))
    solution()
