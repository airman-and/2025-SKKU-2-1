import pandas as pd
import numpy as np
file_path = 'data/score_2.csv' # 파일 경로
score_2 = pd.read_csv(file_path)

file_path_additional = 'data/score_2_add.csv'
score_2_add = pd.read_csv(file_path_additional)

pd.set_option('mode.chained_assignment',  None)

print('과락 반영 점수표')
print(score_2)
print('전학생 시험 점수표')
print(score_2_add)

##여기에 코드를 작성하세요##
score_final = pd.concat([score_2,score_2_add],axis=0)
score_final['평균'] = score_final[['문학','수학','역사','과학']].mean(axis=1)
# 아주 손쉽게 '평균'이라는 열을 추가할 수 있음을 알 수 있었고, 또한 이름 열을 제외한 문학,수학,역사,과학이 들어가야 waning이 일어나지 않음을 알 수 있다.

#########################
print('최종 점수표')
print(score_final)