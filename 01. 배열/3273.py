# 두 수의 합

n = int(input())
lst = list(map(int, input().split()))
x = int(input())

lst.sort()

left, right = 0, n-1
cnt = 0

while left<right:
    temp = lst[left]+lst[right]
    if temp == x:
        cnt += 1
        left += 1
    elif temp<x:
        left += 1
    else:
        right -= 1
print(cnt)