# 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    for i in arr:
        if not answer or answer[-1] != i:
            answer.append(i)
    return answer