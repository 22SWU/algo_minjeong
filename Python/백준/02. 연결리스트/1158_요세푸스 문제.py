# 1158: 요세푸스 문제
# https://infinitt.tistory.com/213

n, k = list(map(int, input().split()))

arr = [i for i in range(1, n+1)]    # 처음 원에 앉을 사람들
answer = []     # 제거된 사람들을 넣을 배열
num = 0     # 제거될 사람의 인덱스 번호

for i in range(n):
    num += k-1
    if num >= len(arr):
        num = num%len(arr)
    
    answer.append(str(arr.pop(num)))

print("<", ", ".join(answer), ">", sep='')