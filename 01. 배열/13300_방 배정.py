# 13300: 방 배정
import math

N, K = list(map(int, input().split()))

students = [[0]*7 for _ in range(2)]

for _ in range(N):
    S, Y = list(map(int, input().split()))
    students[S][Y] += 1

total = 0
for i in students:
    for j in i:
        total += math.ceil(j/K)

print(total)