import pandas as pd
import numpy as np
file_path = 'data/score_4.csv' # 파일 경로
score_4 = pd.read_csv(file_path)

file_path_attend = 'data/attend.csv'
attend = pd.read_csv(file_path_attend)

pd.set_option('mode.chained_assignment',  None)

every = pd.merge(score_4,attend,on='이름',how='inner')

# 평균 상위 3명
final_top_3_attend = every.nlargest(3, '평균')[['이름', '출석률']]

# 평균 하위 5명 (↓ 출석률 기준 높은 순으로 정렬)
final_bottom_5_attend = every.nsmallest(5, '평균').sort_values(by='출석률', ascending=False)[['이름', '출석률']]

# 출석률 상위 3명
final_top_3_mean = every.nlargest(3, '출석률')[['이름', '평균']]

# 출석률 하위 5명 (↓ 평균 높은 순으로 정렬)
final_bottom_5_mean = every.nsmallest(5, '출석률').sort_values(by='평균', ascending=False)[['이름', '평균']]


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