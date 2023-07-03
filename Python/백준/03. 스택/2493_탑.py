# 2493: 탑

n = int(input())
tops = list(map(int, input().split()))

stack = []
answer = [0]*n

# 왼쪽부터 값 삽입, 의미 없는 탑 제거
for i in range(n):
    while stack:
        if stack[-1][1] > tops[i]:
            # 현재 탐색하고 있는 탑의 높이가 Stack TOP의 높이보다 작다면, 수신 가능
            answer[i] = (stack[-1][0]+1)
            break
        else:
            # Stack TOP 제거
            stack.pop()
    # 현재 탑의 정보를 Stack에 삽입
    stack.append([i, tops[i]])      # 인덱스, 값


print(" ".join(map(str, answer)))