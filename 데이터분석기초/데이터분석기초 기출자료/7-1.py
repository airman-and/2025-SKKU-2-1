import pandas as pd
file_path = 'data/score_1.csv' # 파일 경로
pd.set_option('mode.chained_assignment',  None)
score_1 = pd.read_csv(file_path)

print('원본 점수표')
print(score_1)

##여기에 코드를 작성하세요##
# 역사 과목이 60점 미만일 경우 그 행 데이터를 삭제해야한다.
# for문을 사용해서 csv 파일을 돌아가며 역사<60인 경우는 drop하면된다.
# 이때 inplace=True로 해주자. 
dropped_count=0
for i in score_1.index:
	if score_1.loc[i,'역사'] <60:
		score_1.drop(i, inplace=True)
		dropped_count += 1
dropped_score_1=score_1



#########################
print('과락 반영 점수표')
print(dropped_score_1)

print('과락 대상 학생 수:', dropped_count)