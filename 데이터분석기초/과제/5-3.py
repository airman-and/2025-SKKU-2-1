# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
# 반 개수 학생 명수 받기!
N,M = map(int, input().split())
structure = np.zeros((N,M), dtype=int)




# 반, 그룹, 학생을 손댈 while 문 만들기
while True:
	input_string = input()
	if input_string == "INPUT_END":
		break
	input_string = input_string.split()
	if input_string[0] == 'CLASS':
		structure[int(input_string[1]), :] += int(input_string[3])
		
	elif input_string[0] == 'GROUP':
		structure[:, int(input_string[2])] += int(input_string[3])
		
	elif input_string[0] == 'STUDENT':
		structure[int(input_string[1]), int(input_string[2])] += int(input_string[3])
	
# :의 역할은  행,: 이면 해당 행 전부에 열,:이면 해당 열 전부에 값을 더해준다는 것이다.


class_number = int(input())
class_score_average = sum(structure[class_number,:])/M





print(f"{class_score_average:.2f}")