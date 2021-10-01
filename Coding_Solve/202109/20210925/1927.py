import heapq
import sys
input = sys.stdin.readline


def solution():
    heap = []
    for _ in range(N):
        num = int(input())
        if num == 0:
            try:
                print(heapq.heappop(heap))
            except Exception:
                print(0)
        else:
            heapq.heappush(heap, num)


if __name__ == "__main__":
    N = int(input())
    solution()
