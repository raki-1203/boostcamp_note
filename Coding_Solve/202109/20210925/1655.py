import heapq
import sys
input = sys.stdin.readline

def solution1():
    num = int(input())
    max_heap = [(-num, num)]
    min_heap = []
    print(max_heap[0][1])
    for _ in range(N-1):
        num = int(input())

        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, (-num, num))
        else:
            heapq.heappush(min_heap, num)

        if max_heap[0][1] > min_heap[0]:
            a = heapq.heappop(max_heap)[1]
            b = heapq.heappop(min_heap)
            heapq.heappush(max_heap, (-b, b))
            heapq.heappush(min_heap, a)

        print(max_heap[0][1])


def solution():
    max_heap = []
    min_heap = []
    for _ in range(N):
        num = int(input())

        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, (-num, num))
        else:
            heapq.heappush(min_heap, num)

        if min_heap and max_heap[0][1] > min_heap[0]:
            a = heapq.heappop(max_heap)[1]
            b = heapq.heappop(min_heap)
            heapq.heappush(max_heap, (-b, b))
            heapq.heappush(min_heap, a)

        print(max_heap[0][1])


if __name__ == "__main__":
    N = int(input())
    solution()
