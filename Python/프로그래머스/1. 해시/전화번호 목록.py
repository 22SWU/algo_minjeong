# 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    # 오름차순 정렬
    phone_book.sort()
    # 전화번호 2개씩 비교해 접두어인 지 확인
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False     
    return True

# def solution(phone_book):
#     # 해시맵 만들기
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
    
#     # 접두어가 해시맵에 존재하는 지 찾기
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             # 접두어가 해시맵에 있고, 검사 중인 phone_number가 아니라면
#             if temp in hash_map and temp != phone_number:
#                 return False
#     return True