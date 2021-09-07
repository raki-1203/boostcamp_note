from collections import deque


def solution(s):
    answer = []
    for x in s:
        stack = []
        count = 0
        for string in x:
            # 문자열이 0이면
            if string == '0':
                # 앞에 2개가 1, 1인지 확인
                if stack[-2:] == ['1', '1']:
                    count += 1
                    stack.pop()
                    stack.pop()

                # 앞에 2개가 1, 1이 아니면 그냥 0을 추가
                else:
                    stack.append(string)
                    # 문자열이 0이 아니면 그냥 추가
            else:
                stack.append(string)

        # 110이 없기 때문에 변화 불가능
        if count == 0:
            answer.append(x)

        # 110이 있다면
        else:
            final = deque()

            # 0이 나오기 전까지는 append
            while stack:
                if stack[-1] == '1':
                    final.append(stack.pop())
                elif stack[-1] == '0':
                    break

            # 0이 나왔다면 110을 주어진 count 만큼 append
            while count > 0:
                final.appendleft('0')
                final.appendleft('1')
                final.appendleft('1')
                count -= 1

            # stack에 남아있는거 다 추가
            while stack:
                final.appendleft(stack.pop())
            answer.append(''.join(final))

    return answer


if __name__ == '__main__':
    s = ["1110", "100111100", "0111111010"]
    ans = solution(s)
    print(ans)
    print(s)
