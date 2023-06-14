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
