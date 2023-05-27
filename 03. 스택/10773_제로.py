# 10773: 제로

K = int(input())
stack = []

for i in range(K):
    inNum = int(input())
    if inNum==0 and stack:
        stack.pop()
    else:
        stack.append(inNum)

print(sum(stack))