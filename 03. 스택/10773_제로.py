# 10773: 제로

import sys

k = int(input())
stack = []

for _ in range(k):
    num = int(sys.stdin.readline())

    if stack and num==0:
        stack.pop()
    elif num>0:
        stack.append(num)

print(sum(stack))