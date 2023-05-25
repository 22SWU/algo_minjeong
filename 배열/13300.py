# 방 배정
import math

N, K = list(map(int, input().split()))

students = [[0]*7 for _ in range(3)]  #성별 / 학년별

for _ in range(N):
    S, Y = map(int, input().split())
    students[S][Y] += 1

room = 0

for i in students:
    for j in i:
        room += math.ceil(j / K)

print(room)
