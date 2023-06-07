# 5397: 키로거

for _ in range(int(input())):
    keyIn = input()
    left = []
    right = []

    for key in keyIn:
        if key=="<":
            if left:
                right.append(left.pop())
        elif key==">":
            if right:
                left.append(right.pop())
        elif key=="-":
            if left:
                left.pop()
        else:
            left.append(key)
    
    answer = left+right[::-1]
    print(''.join(answer))