from collections import deque
import sys
input = sys.stdin.readline


def solution():
    stack = []
    answer = []
    cnt = 0
    for i in range(n):
        num = int(input())

        while cnt < num:
            cnt += 1
            stack.append(cnt)
            answer.append('+')

        if stack[-1] == num:
            stack.pop()
            answer.append('-')
        else:
            print('NO')
            return

    for s in answer:
        print(s)


if __name__ == "__main__":
    n = int(input())
    solution()
