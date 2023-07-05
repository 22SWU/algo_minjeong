# 1021: 회전하는 큐

from collections import deque
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))          # n: 큐의 크기 N, m: 뽑아내려고 하는 수의 개수
position = list(map(int, input().split()))      # 뽑을 수의 위치
deq = deque([i for i in range(1, n+1)])         # deque([1, 2, 3, ..., n])

count = 0
for p in position:
    while True:
        if p == deq[0]:                     # 덱의 첫 인덱스가 뽑아내려는 수라면 뽑기
            deq.popleft()
            break
        else:
            if deq.index(p) > len(deq)/2:   # 뽑아내려는 수의 인덱스가 덱의 길이를 반으로나 나눈 것보다 크다면
                deq.appendleft(deq.pop())   # 오른쪽으로 움직이기
            else:
                deq.append(deq.popleft())   # 왼쪽으로 움직이기
            count+=1

print(count)