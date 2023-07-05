# 6189: 옥상 정원 꾸미기

import sys
input = sys.stdin.readline

n = int(input())
stack = []
cnt = 0

for i in range(n):
    num = int(input())
    # stack의 마지막 원소가 새로 들어올 데이터보다 작으면
    # 새로운 빌딩을 볼 수 없으므로 pop
    while (stack and stack[-1]<=num):
        stack.pop()
    cnt += len(stack)    # 현재 검사하는 빌딩을 볼 수 있는 빌딩 개수를 더하기
    stack.append(num)

print(cnt)


# input
# 10, 3, 7, 4, 12, 2

# 3을 보는 수: 10
# [10, 3]

# 7을 보는 수: 10
# [10, 7]

# 4을 보는 수: 10, 7
# [10, 7, 4]

# 12을 보는 수: x
# [12]

# 2을 보는 수: 12
# [12, 2]
