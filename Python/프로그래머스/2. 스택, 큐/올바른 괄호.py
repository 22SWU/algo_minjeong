# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(strs):
    answer = True
    stack = []
    
    for s in strs:
        # '('는 stack에 추가
        if s == "(":
            stack.append(s)

        # i == ')'인 경우
        else:
            if stack and stack.pop()=='(':      # '('가 ')'와 짝을 이루면 stack에서 '(' 하나 제거
                continue
            else:                               # 괄호 짝이 ')'로 시작하면 False 반환
                return False
    if stack:
        return False
    return True