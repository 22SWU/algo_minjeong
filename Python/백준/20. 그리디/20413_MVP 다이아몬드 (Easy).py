# 20413: MVP 다이아몬드 (Easy)

import sys
input = sys.stdin.readline

m = int(input())
s, g, p, d = list(map(int, input().split(" ")))
mvp = list(input().strip())

total = 0
prev = 0

for i in range(len(mvp)):
	if mvp[i] == "B":
		total += s-1-prev
		prev = s-1-prev
	elif mvp[i] == "S":
		total += g-1-prev
		prev = g-1-prev
	elif mvp[i] == "G":
		total += p-1-prev
		prev = p-1-prev
	elif mvp[i] == "P":
		total += d-1-prev
		prev = d-1-prev
	elif mvp[i] == "D":
		total += d
		prev = d
print(total)
		