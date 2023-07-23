# 15649: N과 M (1) 
# https://www.acmicpc.net/problem/15649
# https://jiwon-coding.tistory.com/21

n, m = list(map(int, input().split()))

ans = []

def dfs():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return

    for i in range(1, n+1):
        if i not in ans:
            ans.append(i)
            dfs()
            ans.pop()

dfs()