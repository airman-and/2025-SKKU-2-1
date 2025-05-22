import pandas as pd
file_path = 'data/data_after_2.csv' #파일 경로

##여기에 코드를 작성하세요##
df = pd.read_csv(file_path)
score_columns = ['국어', '수학', '영어']
condition = (df[score_columns] > 90).all(axis=1)
filtered_df = df[condition]





########################
print(filtered_df)
#axis=0을 이용하면 행에 대한 결과가 남고 axis=1을 이용하면 열에 대한 결과가 나온다는 것을 알아둬야겠다.


