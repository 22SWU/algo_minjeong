# 1874: 스택 수열

n = int(input())

stack = []
answer = []
now = 1
flag = True

for i in range(n):
    checkNum = int(input())
    while now <= checkNum:
        stack.append(now)
        answer.append('+')
        now += 1
    
    if stack[-1] == checkNum:
        stack.pop()
        answer.append('-')
    else:
        flag = False
        break

if flag:
    print(*answer, sep='\n')
else:
    print("NO")