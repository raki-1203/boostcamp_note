from sys import stdin
input = stdin.readline

def solution(digit_arr):
    for digit_list in digit_arr:
        # 10진수를 2진수로 변환
        digit_sum = sum([int(digit, base=2) for digit in digit_list])
        
        # 2진수 변환
        print(bin(digit_sum)[2:])
            
        
if __name__ == '__main__':
    T = int(input())
    digit_arr = [input().split() for _ in range(T)]
    solution(digit_arr)
       
