import sys
input = sys.stdin.readline


def solution():
    X = int(input())

    answer = 0
    X = bin(X)
    for x in X:
        if x == '1':
            answer += 1
    print(answer)


if __name__ == '__main__':
    solution()