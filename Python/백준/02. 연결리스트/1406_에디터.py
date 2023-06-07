# 1406: 에디터
from sys import stdin

left = list(input())
right = []
n = int(input())

for _ in range(n):
    cmd = list(stdin.readline().split())

    if cmd[0]=="L" and left:
        right.append(left.pop())
    elif cmd[0]=="D" and right:
        left.append(right.pop())
    elif cmd[0]=="B" and left:
        left.pop()
    elif cmd[0]=="P":
        left.append(cmd[1])
    
answer = left + right[::-1]
print(''.join(answer))