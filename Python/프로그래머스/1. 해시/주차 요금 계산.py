# 주차 요금 계산 (NOT YET)
# https://school.programmers.co.kr/learn/courses/30/lessons/92341?language=python3

def solution(fees, records):
    answer = []
    carIn = {}
    
    for car in records:
        carInform = car.split(" ")
        time = carInform[0]
        carNum = carInform[1]
        inout = carInform[2]
        
        if inout == "IN":
            carIn[carNum] = time
        else:
            print("error")
    
    return answer