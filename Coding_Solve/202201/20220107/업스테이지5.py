def solution(n, k):
    answer = -1

    num_dict = {i: set([(i * j) % 10 for j in range(1, 11)]) for i in range(1, 10**6)}

    if (n % 10) in num_dict[k]:
        for i in range(1, 10**4):
            target = int(str(n) * i)
            if target % k == 0:
                answer = i
                break
    else:
        answer = -1
    return answer