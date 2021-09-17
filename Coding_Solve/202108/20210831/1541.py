from sys import stdin
input = stdin.readline


def solution(formula):
    # - 로 나눈 후 + 로 묶인 값들을 저장할 리스트
    num_list = []

    # 수식을 - 로 나눈 리스트
    minus_split_list = formula.split('-')
    for minus_split in minus_split_list:
        # - 로 나눈 분리된 문자열의 더한 값
        cnt = 0
        # + 로 나눈 리스트
        plus_split_list = minus_split.split('+')
        for plus_split in plus_split_list:
            # 각각의 + 로 나뉜 값을 정수로 변환후 더함
            cnt += int(plus_split)

        # 리스트에 추가
        num_list.append(cnt)

    answer = 0
    for i in range(len(num_list)):
        if i == 0:
            answer += num_list[i]
        else:
            answer -= num_list[i]

    print(answer)


if __name__ == '__main__':
    formula = input().strip()

    solution(formula)
