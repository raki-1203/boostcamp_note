from sys import stdin
input = stdin.readline

N = int(input())
a = [input().strip() for _ in range(N)]

a = ['hello', 'hi', 'h', 'run', 'rerun', 'running']
N = 6

a.sort(key=len)

result = []
for i in range(N):
    standard_word = a[i]
    is_head = False
    for j in range(i+1, N):
        try:
            word = a[j]
            if word.startswith(standard_word):
                is_head = True
                break
        except Exception:
            continue
    if is_head == False:
        result.append(standard_word)
        
print(len(result))
