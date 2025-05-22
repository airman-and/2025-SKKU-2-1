import pandas as pd
file_path = 'data/data_after_2.csv' #파일 경로
##여기에 코드를 작성하세요##
df = pd.read_csv(file_path)
df['국어'] = df['국어']+10
df['국어'] = df['국어'].clip(upper=100)
########################
print(df)
#보통 판다스에서 행렬[열의 이름]+무언가로 수정하는 경우가 많다.


