from collections import deque
from sys import stdin
input = stdin.readline

def solution(N, K, X, road_list):
    # node 에서 다른 node로의 경로
    graph = {node: [] for node in range(1, N + 1)}
    for road in road_list:
        graph[road[0]].append(road[1])

    # 최단 거리 저장하는 dictionary
    distance_dict = {node: 9999 for node in range(1, N + 1)}
    distance_dict[X] = 0

    # 시작 node queue에 저장
    queue = deque([(distance_dict[X], X)])

    while queue:
        cur_distance, cur_destination = queue.popleft()
        
        # 현재 node에서의 경로 모두 탐색
        for new_destination in graph[cur_destination]:
            distance = cur_distance + 1
            # 현재 node의 거리와 최단거리를 비교
            if distance < distance_dict[new_destination]:
                distance_dict[new_destination] = distance
                queue.append((distance, new_destination))

    # 최단거리가 K인 node 만 뽑아서 오름차순 정렬
    result =  sorted([node for node, distance in distance_dict.items() \
                      if distance == K])
    if len(result) == 0:
        result.append(-1)

    for r in result:
        print(r)
    
        
if __name__ == '__main__':
    # 도시의 개수 N
    # 도로의 개수 M
    # 거리 정보 K
    # 출발 도시의 번호 X
    N, M, K, X = list(map(int, input().split()))
    road_list = [list(map(int, input().split())) for _ in range(M)]
    solution(N, K, X, road_list)
