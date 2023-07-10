# 21758: 꿀 따기

import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split(" ")))

# 누적합 ->
# 9 18 22 23 27 36 45

lrSum = []
# for i in range(0, len(lst)):
#     a = int(lrSum[-1]) + int(lst[i]) if lrSum else int(lst[i])
#     lrSum.append(a)
# print(lrSum)
lrSum.append(lst[0])
for i in range(1, len(lst)):
    lrSum.append(lrSum[i-1] + lst[i])

# 벌, 벌, 통
total = 0
for i in range(1,n-1):
    total = max(total, lrSum[-1]-lrSum[i]-lst[i] + lrSum[-1]-lrSum[0])

# 통, 벌, 벌
for i in range(1,n-1):
    total = max(total, lrSum[-2]-lst[i] + lrSum[i-1])

# 벌, 통, 벌
for i in range(1,n-1):
    total = max(total, lrSum[-2]-lrSum[0] + lst[i])

print(total)
