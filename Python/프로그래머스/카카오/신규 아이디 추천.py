# 신규 아이디 추천

# --------------------------- 정규 표현식 ---------------------------
# re.sub('From', 'To', String)
import re

def solution(new_id):
    # 1단계
    answer = new_id.lower()

    # 2단계
    answer = re.sub('[^a-z0-9-_.]', '', answer)

    # 3단계
    answer = re.sub('[.]{2,}', '.', answer)

    # 4단계
    answer = re.sub('^[.]|[.]$', '', answer)

    # 5단계
    if answer == '':
        answer ='a'

    # 6단계
    answer = answer[:15]
    answer = re.sub('[.]$', '', answer)

    # 7단계
    while len(answer) < 3:
        answer += answer[-1]
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))



# --------------------------- 정규 표현식 X ---------------------------
# def solution(new_id):
#     answer = ''
    
#     # 1단계
#     new_id = new_id.lower()
    
#     # 2단계
#     for word in new_id:
#         if word in '-_.' or word.isdigit() or word.isalpha():   # isdigit + isalpah = isalnum
#             answer += word
            
#     # 3단계
#     while '..' in answer:
#         answer = answer.replace('..', '.')
        
#     # 4단계
#     if answer[0:1]=='.':
#         answer = answer[1:]
#     if answer[-1:]=='.':
#         answer = answer[:-1]
        
#     # 5단계
#     if answer == '':
#         answer = 'a'
    
#     # 6단계
#     if len(answer) >= 16:
#         answer = answer[:15]
#         if answer[-1] == '.':
#             answer = answer[:-1]
    
#     # 7단계
#     while len(answer) < 3:
#         answer += answer[-1]
    
#     return answer
