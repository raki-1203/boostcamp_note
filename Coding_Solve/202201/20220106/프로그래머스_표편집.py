from collections import deque

def solution(n, k, cmd):
    answer = ''

    # 현재위치 기억하는 변수 필요
    # 명령에 따라서 if ~ else 수행하는 코드 필요
    # 지워진 행 정보 담아둘 stack 필요
    # 복원했을 때 현재위치 기억하는 변수에 위치도 변할 수 있음

    current_k = k
    S = set(list(range(n)))
    stack = deque()
    for c in cmd:
        c = c.split()
        if c[0] == 'U':
            current_k -= int(c[1])
        elif c[0] == 'D':
            current_k += int(c[1])
        elif c[0] == 'C':
            stack.append(S.copy())
            S.remove(current_k)
            if len(S) == current_k:
                current_k -= 1
        elif c[0] == 'Z':
            prev_S = stack.pop()
            intersection = prev_S - S
            S = prev_S
            num = intersection.pop()
            if current_k >= num:
                current_k += 1

    for i in range(n):
        if i not in S:
            answer += 'X'
        else:
            answer += 'O'

    return answer


if __name__ == '__main__':
    n = 8
    k = 2
    cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
    print(solution(n, k, cmd))