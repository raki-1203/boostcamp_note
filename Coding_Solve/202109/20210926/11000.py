import heapq
import sys
input = sys.stdin.readline


def solution():
    # 시작 시간으로 정렬
    class_time.sort()

    heap = []
    heapq.heappush(heap, class_time[0][1])

    for start, end in class_time[1:]:
        # heap 에 들어있는 가장 빨리 끝나는 강의 시간이 시작시간보다 크면 강의실 추가
        if heap[0] > start:
            heapq.heappush(heap, end)
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, end)

    print(len(heap))

if __name__ == "__main__":
    N = int(input())
    class_time = [list(map(int, input().split())) for _ in range(N)]
    solution()
