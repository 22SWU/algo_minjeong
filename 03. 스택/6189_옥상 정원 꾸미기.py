# 6189: 옥상 정원 꾸미기
import sys

num = int(sys.stdin.readline())
list=[]
cnt = 0
 
for i in range(num):
    num = int(sys.stdin.readline())
    while len(list)!=0 and num>=list[-1]:
        list.pop()
    cnt +=len(list)
    list.append(num)
 
print(cnt)

# N = int(input())

# # heights = [int(sys.stdin.readline()) for _ in range(N)]

# lst = []

# for i in range(N-1):
#     height = int(sys.stdin.readline())


# cnt = 0
# for i in range(N-1):
#     cur = heights[i]
#     for j in range(i+1, N):
#         barrier = heights[j]
#         # 탈출문
#         if barrier >= cur:
#             break
        
#         cnt += 1

# print(cnt)