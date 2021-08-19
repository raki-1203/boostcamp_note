from sys import stdin
input = stdin.readline

def solution(n):
    # 피보나치 수열 array 
    fibonacci_arr = [0, 1]
    for i in range(2, 50):
        fibonacci_arr.append(fibonacci_arr[i - 1] + fibonacci_arr[i - 2])

    
    result = []
    # 가장 큰 수부터 거꾸로 탐색
    for i, num in enumerate(fibonacci_arr[::-1]):
        if num <= n:
            result.append(num)
            n -= num
            if n == 0:
                break
                
    print(*sorted(result))

    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        solution(n)
