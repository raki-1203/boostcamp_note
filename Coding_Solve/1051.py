from sys import stdin


n, m = map(int, stdin.readline().split())
boards = []

for _ in range(n):
    boards.append([int(x) for x in stdin.readline().rstrip()])

max_square = [[1] * (m - 1) for _ in range(n - 1)]

for r in range(n - 1):
    for c in range(m - 1):
        x = boards[r][c]
        # (r, c)를 왼쪽 위 꼭짓점으로 가지는 가장 큰 정사각형의 크기 지정
        i = min(n - r, m - c) - 1

        while i > 0 and max_square[r][c] == 1:
            if boards[r][c + i] == x and boards[r + i][c] == x \
                and boards[r + i][c + i] == x:
                max_square[r][c] = (i + 1) * (i + 1)
            i -= 1
print(max_square)

max_value = 1

for r in range(n - 1):
    for c in range(m - 1):
        max_value = max(max_value, max_square[r][c])

print(max_value)
