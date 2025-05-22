import pandas as pd
file_path = 'data/data.csv' # 파일 경로

##여기에 코드를 작성하세요##
df = pd.read_csv(file_path)
print(df.head())
#########################
# 머리부분 5개 출력