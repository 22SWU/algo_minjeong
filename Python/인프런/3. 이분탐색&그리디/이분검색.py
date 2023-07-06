# 이분검색

import sys
sys.stdin = open("C:/Users/serak/study/algo_minjeong/Python/인프런/1. 코드 구현력/input.txt", "rt")
n, m = list(map(int, input().split()))
lst = list(map(int, input().split()))

lst.sort()

left = 0
right = n-1

while left <= right:
    mid = (left+right)//2
    if lst[mid]==m:
        print(mid+1)
        break
    elif lst[mid]>m:
        right = mid-1
    else:
        left = mid+1