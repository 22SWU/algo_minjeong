# 5430: AC

# from collections import deque
# import sys
# input = sys.stdin.readline
# T = int(input())

# for test_case in range(1, T+1):
#     func = input().rstrip()
#     n = int(input())
#     lst_input = input().rstrip()[1:-1]
#     lst = deque(list(map(int, lst_input .split(",")))) if lst_input else deque()
#     answer = "error"

#     if n!=0:
#         for i in range(len(func)):
#             if func[i]=="R" and lst:
#                 lst.reverse()
#                 # lst = lst[::-1] 덱은 해당 방식으로 슬라이싱 안됨
#             elif func[i]=="D" and lst:
#                 lst.popleft()
#         if lst:
#             result = ''.join(map(str, lst))
#             print('[' + ",".join(result) + ']')
#         else:
#             print("error")    
    
#     else:
#         print("error")



from collections import deque

T = int(input())

for tc in range(T):
    cmds = input()
    n = int(input())
    deq = deque(input()[1:-1].split(','))       # deq: 괄호와 쉼표 제외하고 큐에 담기
    flag = 0                                    # 뒤집기(R) 개수 카운트
    
    # deque는 [''] 의 길이를 0이 아닌 1로 취급하기 때문에 초기화
    if n == 0:  
        deq = []            
    
    for cmd in cmds:
        if cmd == 'R':
            flag += 1
        elif cmd == 'D':
            if deq:
                if flag % 2 == 1:   # 역방향
                    deq.pop()
                else:               # 순방향
                    deq.popleft()
            else:
                print('error')  
                break                   
    else:
        # 역방향
        if flag % 2 == 1:
            deq.reverse()
        print('[' + ','.join(deq) + ']')