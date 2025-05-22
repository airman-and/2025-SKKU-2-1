import pandas as pd
data_path='data/midterm_4.csv'

df = pd.read_csv(data_path)

category = input()

df_2 = df[df['카테고리'] == category]

df_3 = df_2[df_2['출금'] > 0]

df_4 = df_3['출금'].sort_values(ascending = False)

out = df_4
# 채점을 위한 코드입니다. out이 Series가 되도록 해주세요
print((out.iloc[0]),(out.iloc[-1]))