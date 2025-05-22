import pandas as pd
import numpy as np
file_path = 'data/score_3.csv' # 파일 경로
score_3 = pd.read_csv(file_path)

file_path_grades = 'data/grades.csv'
grades = pd.read_csv(file_path_grades)

pd.set_option('mode.chained_assignment',  None)
##여기에 코드를 작성하세요##
import sys
grades_score= pd.merge(grades,score_3,on='이름',how='inner')

target_columns = ['문학', '수학', '역사', '과학']
mean_by_grade = grades_score.groupby('학점')[target_columns].mean()


mean_by_grade['평균'] = mean_by_grade.mean(axis=1)


#########################
print('학점이 기재된 점수표')
print(grades_score)

print('학점별 평균 점수표')
print(mean_by_grade)
