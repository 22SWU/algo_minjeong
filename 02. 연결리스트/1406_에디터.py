# 1406: 에디터

# word = list(input())
# n = int(input())

# cmdPos = len(word)

# for i in range(n):
#     cmd = input().split()
#     if cmd[0]=="L":
#             if cmdPos!=0:
#                 cmdPos -= 1
#     elif cmd[0]=="D":
#         if cmdPos!=len(word):
#             cmdPos += 1
#     elif cmd[0]=="B":
#         if cmdPos!=0:
#             word.pop(cmdPos-1)
#         cmdPos -= 1
#     elif cmd[0]=="P":
#         newWord = cmd[1]
#         word.insert(cmdPos, newWord)
#         cmdPos += 1
        

# for i in word:
#     print(i, end="")

from sys import stdin

left = list(input())
right = []

for _ in range(int(input())):
    command = list(stdin.readline().split())
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

answer = left + right[::-1]
print(''.join(answer))