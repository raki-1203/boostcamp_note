def solution(maps):
    answer = -1

    nrow = len(maps)
    ncol = len(maps[0])
    visited = [[True] * ncol for _ in range(nrow)]

    max_cnt = 0
    for i in range(nrow):
        for j in range(ncol):
            cnt = 0
            if maps[i][j] == 1 and visited[i][j]:
                visited[i][j] = False
                stack = [[i, j]]
                while stack:
                    r, c = stack.pop()

                    for D in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        nr = r + D[0]
                        nc = c + D[1]

                        if (0 <= nr < nrow) and (0 <= nc < ncol):
                            if visited[nr][nc]:
                                if maps[nr][nc] == 1:
                                    visited[nr][nc] = False
                                    stack.append([nr, nc])
                                else:
                                    cnt += 1
                        else:
                            cnt += 1

            max_cnt = max(cnt, max_cnt)

    answer = max_cnt

    return answer

if __name__ == '__main__':
    # maps = [[0,0,1,0,0],[0,1,1,0,1],[0,0,1,0,1],[1,1,1,0,1]]
    maps = [[1,0,1,1],[0,0,1,1],[1,1,0,1],[1,1,0,0]]
    maps = [[0, 0], [0, 0]]
    print(solution(maps))