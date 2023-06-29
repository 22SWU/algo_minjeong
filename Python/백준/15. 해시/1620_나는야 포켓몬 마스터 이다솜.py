# 1620: 나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
 
# 딕셔너리에 {포켓몬 이름 : 번호}, {번호 : 포켓몬 이름} 값을 저장
dict = {}
for i in range(1, n + 1):
    str = input().rstrip()
    dict[i] = str
    dict[str] = i

# value를 찾지 않고 key 값만 빠르게 찾을 수 있음
for _ in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])
        