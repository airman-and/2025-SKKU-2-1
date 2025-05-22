# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np

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
	elif input_string[0] == 'REFORM':
		structure=structure.reshape(int(input_string[1]),-1)
	
# -1은 행이나 열을 자동 계산하도록 만든다.
# reshape에서 이용된다.
# 그렇기에 리폼은 행의 개수에 맞게 학생수를 나누어 달라는 것이다.


class_number = int(input())
class_score_average = sum(structure[class_number,:])/(structure.shape[1])


print(f"{class_score_average:.2f}")