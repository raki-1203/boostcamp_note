def solution(n):
    answer = -1

    cnt = 0
    for i in range(1, 1000):
        k = 5 ** i
        if k > n:
            break
        cnt += n // k

    answer = cnt
    return cnt

if __name__ == '__main__':
    n = 5
    n = 10
    print(solution(n))
    