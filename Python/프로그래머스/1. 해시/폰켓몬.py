# 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):    
    set_len = len(set(nums))
    
    if set_len >=  len(nums)/2:
        return len(nums)/2
    return set_len