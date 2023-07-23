# 11286: 절댓값 힙
# https://www.acmicpc.net/problem/11286

import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
	num = int(sys.stdin.readline())
	if num:
		heapq.heappush(heap, (abs(num), num))
	else:
		if heap:
			print(heapq.heappop(heap)[1])
		else:
			print(0)
			
	print(list(heap))
