# 방 번호

roomNum = input()
lst = [0]*9

for n in roomNum:
    intN = int(n)
    if intN == 9:
        intN = 6
    lst[intN] += 1
lst[6] = (lst[6]+1)//2

print(max(lst))