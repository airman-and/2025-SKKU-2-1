import pandas as pd
import numpy as np
file_path = 'data/score_4.csv' # 파일 경로
score_4 = pd.read_csv(file_path)

file_path_attend = 'data/attend.csv'
attend = pd.read_csv(file_path_attend)

pd.set_option('mode.chained_assignment',  None)

every = pd.merge(score_4,attend,on='이름',how='inner')

final_top_3_attend =every.sort_values(by='평균', ascending=False).head(3)[['이름','출석률']]
final_bottom_5_attend = every.sort_values(by='평균').head(5).sort_values(by='평균', ascending=False)[['이름','출석률']]

final_top_3_mean = every.sort_values(by='출석률', ascending=False).head(3)[['이름','평균']]
final_bottom_5_mean = every.sort_values(by='출석률' ).head(5).sort_values(by='출석률', ascending=False)[['이름','평균']]



print("평균 점수 상위 3명의 출석률")
print(final_top_3_attend)
print()

print("평균 점수 하위 5명의 출석률")
print(final_bottom_5_attend)
print()

print("출석률 기준 상위 3명의 평균 점수")
print(final_top_3_mean)
print()

print("출석률 기준 하위 5명의 평균 점수")
print(final_bottom_5_mean)