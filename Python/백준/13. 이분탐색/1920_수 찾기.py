# 1920: 수 찾기
# https://www.acmicpc.net/problem/1920

n = int(input())
nums1 = list(map(int, input().split()))
nums1.sort()
m = int(input())
nums2 = list(map(int, input().split()))

for i in nums2:
    left = 0
    right = n-1
    mid = n//2
    flag = False

    while left<=right:
        if i == nums1[mid]:
            flag = True
            break

        if i<nums1[mid]:
            right = mid-1
            mid = (left+right)//2
        else:
            left = mid+1
            mid = (left+right)//2

    if flag == True:
        print(1)
    else:
        print(0)