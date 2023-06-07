# 11328: Strfry

T = int(input())

for _ in range(T):
    str1, str2 = input().split()
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1==str2:
        print("Possible")
    else:
        print("Impossible")