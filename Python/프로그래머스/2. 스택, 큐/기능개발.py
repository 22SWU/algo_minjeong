# 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while progresses:
        # 기능의 진행상황과 그 동안 지난 날짜만큼의 speed를 구해서 더하기
        if (progresses[0] + time*speeds[0] >= 100):
            # 완료되면 리스트에서 제거
            progresses.pop(0)
            speeds.pop(0)
            # 완료된 기능 수
            count += 1
        else:
            # 만약 완료된 기능이 있다면 answer에 더해주고 0으로 초기화
            if count>0:
                answer.append(count)
                count = 0
            # time 추가
            time += 1
    answer.append(count)
    return answer