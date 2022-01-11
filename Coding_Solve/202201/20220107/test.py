from itertools import accumulate


def solution(cards):
    # Write your code here
    kero_cumsum = [0] + list(accumulate(cards[::2]))
    beroni_cumsum = [0] + list(accumulate(cards[1::2]))
    # print(kero_cumsum)
    # print(beroni_cumsum)
    flag = False
    for i in range(len(cards)):
        if i % 2 == 0:
            kero = kero_cumsum[i // 2] + beroni_cumsum[-1] - beroni_cumsum[i // 2]
            beroni = beroni_cumsum[i // 2] + kero_cumsum[-1] - kero_cumsum[i // 2 + 1]
        else:
            kero = kero_cumsum[i // 2 + 1] + beroni_cumsum[-1] - beroni_cumsum[i // 2 + 1]
            beroni = beroni_cumsum[i // 2] + kero_cumsum[-1] - kero_cumsum[i // 2 + 1]
        if kero == beroni:
            flag = True
            break

    if flag:
        return i + 1
    else:
        return -1


if __name__ == '__main__':
    cards = [2, 5, 2, 7, 8, 4]
    cards = [2, 5, 3, 1]

    print(solution(cards))

