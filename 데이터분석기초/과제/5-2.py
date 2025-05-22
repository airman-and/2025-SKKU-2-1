# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
#dk = [1,2,3,4]*12
# 점수를 담아둘 어레이를 생성하세요
number_of_students = int(input())
student_scores= [0]*number_of_students
# 리스트에 정수를 곱하면 그 정수만큼의 크기를 가진 리스트가 반복생성된다.
# 입력되는 점수 변동 반영을 INPUT_END 입력까지 반복하세요

while True:
	string = input()
		
	if string == "INPUT_END":
		break
	try:
		parts = string.split()
		student_num = int(parts[0])
		student_list = int(parts[1])

		if 0<= student_num < number_of_students:
			student_scores[student_num] += student_list

	except (IndexError, ValueError):
		continue



# 특정 학생의 점수를 정수로 출력하세요!
student = int(input())
score_answer = student_scores[student]
print(int(score_answer))



