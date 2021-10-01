# u와 v로 나누는 함수
def divide(w):
    left_cnt = 0
    right_cnt = 0
    for i in range(len(w)):
        if w[i] == '(':
            left_cnt += 1
        elif w[i] == ')':
            right_cnt += 1
        if left_cnt == right_cnt:
            return w[:i + 1], w[i + 1:]


# u가 올바른 괄호 문자열 인지 판단하는 함수
def is_correct(u):
    if u[0] == ')':
        return False
    else:
        left_cnt = 0
        right_cnt = 0
        for i in range(len(u)):
            if u[i] == '(':
                left_cnt += 1
            else:
                right_cnt += 1
            if left_cnt < right_cnt:
                return False
        return True


def solution(p):
    if p == '':
        return ''

    u, v = divide(p)
    if is_correct(u):
        answer = u
        answer += solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = u[1:-1]
        answer += ''.join(['(' if x == ')' else ')' for x in u])

    return answer