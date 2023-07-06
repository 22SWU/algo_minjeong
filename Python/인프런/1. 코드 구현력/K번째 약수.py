# 1. K번째 약수

import sys
sys.stdin = open("C:/Users/serak/study/algo_minjeong/Python/인프런/1. 코드 구현력/input.txt", "rt")

n, k = list(map(int, input().split()))
count = 0
answer = -1

for i in range(1, n+1):
    if n%i==0:
        count += 1
        if count == k:
            answer = i
            break

print(answer)