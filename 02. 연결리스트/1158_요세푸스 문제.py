# 1158: 요세푸스 문제

N, K = list(map(int, input().split()))
que = list(i for i in range(1, N+1))
answer = []
num = 1
while que:
    if num==3:
        num=1
        answer.append(que.pop(0))
    else:
        que.append(que.pop(0))
        num += 1

answer1 = ', '.join(str(i) for i in answer)
print(f"<{answer1}>")