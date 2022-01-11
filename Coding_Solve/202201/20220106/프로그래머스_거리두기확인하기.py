def get_distance(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    return abs(r1 - r2) + abs(c1 - c2)


def solution(places):
    answer = []

    # 파티션을 벽이라고 생각하고 사람과 사람까지의 거리구해서 2보다 작으면 가는 경로 찾아보기
    # 가는 경로에서 테이블이 있는 경우는 그냥 통과 그 경우 거리두기 지키지 않는 경우
    # 갈 수 있는 경로가 없을 때, 거리두기 지키고 있음
    # 모든 사람과 사람사이의 조합을 구해서 비교해야 함

    for place in places:
        # 1. 사람의 좌표 위치 구하기
        board = []
        p_list = []
        for i, p in enumerate(place):
            temp = list(p)
            for j in range(5):
                if temp[j] == 'P':
                    p_list.append([i, j])
            board.append(temp)

        # 2. 모든 사람과 사람사이의 조합 구하기
        flag = True  # 거리두기 유지 여부
        for i in range(len(p_list)):
            for j in range(i + 1, len(p_list)):
                p1, p2 = p_list[i], p_list[j]

                if get_distance(p1, p2) <= 2:
                    r1, c1 = p1
                    r2, c2 = p2

                    visited = [[True] * 5 for _ in range(5)]

                    stack = []
                    stack.append([r1, c1, 0])
                    visited[r1][c1] = False

                    while stack:
                        r, c, cnt = stack.pop()

                        if r == r2 and c == c2:
                            if cnt <= 2:
                                flag = False
                            break

                        for D in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nr = r + D[0]
                            nc = c + D[1]

                            if 0 <= nr < 5 and 0 <= nc < 5 and visited[nr][nc] and board[nr][nc] != 'X':
                                visited[nr][nc] = False
                                stack.append([nr, nc, cnt+1])

                    if not flag:
                        break
            if not flag:
                break

        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer


if __name__ == '__main__':
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
              ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
              ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
              ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))
