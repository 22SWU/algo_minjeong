# 2504: 괄호의 값
# https://www.acmicpc.net/problem/2504

stack = [] # 스택
tmp = 1 # 임시 변수
result = 0 # 결과 변수
lst = list(input()) # 입력값

for i in range(len(lst)):
  if lst[i]=='(':
    tmp *= 2
    stack.append(lst[i])
    
  elif lst[i]=='[':
    tmp *= 3
    stack.append(lst[i])
    
  elif lst[i]==')':
    if not stack or stack[-1]!='(':         #  빈 스택 & 짝 체크
      result = 0
      break
    if lst[i-1]=='(': result += tmp
    tmp //= 2
    stack.pop()
    
  elif lst[i]==']':
    if not stack or stack[-1]!='[':         #  빈 스택 & 짝 체크
      result = 0
      break
    if lst[i-1]=='[': result += tmp
    tmp //= 3
    stack.pop()


# 결과 출력
if stack:
  print(0)
else:
  print(result)