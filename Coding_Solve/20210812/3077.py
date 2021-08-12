from sys import stdin
input = stdin.readline

def solution(N, true_list, pred_list):
    # 전체 개수
    total_num = int(N * (N - 1) / 2)
    # 순서가 맞은 개수
    score = 0

    # 정답 dictionary
    true_dict = {t: i for i, t in enumerate(true_list)}
    # 현우 제출 dictionary
    pred_dict = {p: i for i, p in enumerate(pred_list)}

    for i in range(N):
        for j in range(i+1, N):
            # 만약 정답의 순서가 
            if true_dict[pred_list[i]] < true_dict[pred_list[j]]:
                score += 1
    

    print('{}/{}'.format(score, total_num))



if __name__ == '__main__':
    N = int(input())
    true_list = input().split()
    pred_list = input().split()
    solution(N, true_list, pred_list)
        
    

