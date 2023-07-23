# 모의고사
# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
	student1 = [1, 2, 3, 4, 5]
	student2 = [2, 1, 2, 3, 2, 4, 2, 5]
	student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

	counts = [0,0,0]
	winner = []

	for i in range(len(answers)):
		if answers[i] == student1[i%5]:
			counts[0] += 1
		if answers[i] == student2[i%8]:
			counts[1] += 1
		if answers[i] == student3[i%10]:
			counts[2] += 1
	
	for i in range(3):
		if counts[i] == max(counts):
			winner.append(i+1)
	
	return winner