# 5397: 키로거

# T = int(input())

# for test_case in range(T):
#     inputPW = list(input())
#     pw = []
#     cursor = 0
#     for i in range(len(inputPW)):
#         if inputPW[i]=="<":
#             if cursor !=0: cursor -= 1
#         elif inputPW[i]==">":
#             if cursor != len(pw): cursor += 1
#         elif inputPW[i]=="-":
#             if cursor!=0: cursor = cursor-1
#             pw.pop(cursor)
#         else:
#             pw.insert(cursor, inputPW[i])
#             cursor+=1

#     answer = ''.join(i for i in pw)
#     print(answer)

t = int(input())

for _ in range(t):
    l_list = []
    r_list = []
    data = input()
    for i in data:
        if i == '-':
            if l_list: #왼쪽 스택에 있을 경우
                l_list.pop()
        elif i == '<': # 왼스택에 있는 문자 오른쪽 스택으로
            if l_list:
                r_list.append(l_list.pop())
        elif i == '>': # 오스택에 있는 문자 왼쪽 스택으로
            if r_list:
                l_list.append(r_list.pop())
        else:
            l_list.append(i)
    l_list.extend(reversed(r_list)) # 오른쪽 스택에 있는 문자들은 뒤집어서 붙여야 한다.
    print(''.join(l_list))