from sys import stdin
input = stdin.readline

def solution(char_list):
    for i in range(len(char_list) - 1, 0, -1):
        if char_list[i - 1] < char_list[i]:
            i -= 1
            for j in range(len(char_list) - 1, 0, -1):
                if char_list[i] < char_list[j]:
                    char_list[i], char_list[j] = char_list[j], char_list[i]
                    return char_list[:i + 1] + sorted(char_list[i + 1:])
    return char_list


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        char_list = list(input().strip())
        print(''.join(solution(char_list)))
        
    

