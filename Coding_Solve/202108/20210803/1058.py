from sys import stdin
input = stdin.readline

def solution(N, arr):
    # 2-친구 여부 배열
    frd_arr = [[0 for _ in range(N)] for _ in range(N)]

    # C 역할 k
    for k in range(N):
        # A 역할 i
        for i in range(N):
            # B 역할 j
            for j in range(N):
                if i == j:
                    continue

                # A 와 B 가 친구이거나 A 와 C 가 친구고 B 와 C 가 친구
                if arr[i][j] == 'Y' or (arr[i][k] == 'Y' and arr[k][j] == 'Y'):
                    frd_arr[i][j] = 1
    
    max_num = 0
    for frd in frd_arr:
        max_num = max(max_num, sum(frd))
    
    return max_num
    
    
    
if __name__ == "__main__":
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]
    result = solution(N, arr)
    print(result)
