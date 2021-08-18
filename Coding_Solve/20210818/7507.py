from sys import stdin

input = stdin.readline

def solution(scenario_num, info_list):
    info_list = sorted(info_list, key=lambda x: [x[0], x[2]])
    
    cnt = 0
    prev_d = prev_e = 0
    for d, s, e in info_list:
        if prev_e <= s or prev_d != d:
            cnt += 1
            prev_d, prev_e = d, e
            
    print('Scenario #{}:\n{}\n'.format(scenario_num, cnt))
        
        
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        game_num = int(input())
        info_list = [list(map(int, input().split())) for _ in range(game_num)]
        solution(i, info_list)
