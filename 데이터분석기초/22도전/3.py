import pandas as pd

df = pd.read_csv('C:\\Users\\andycho\\OneDrive\\Desktop\\2025 2학년 1학기\\22도전\\vaccine_data_500.csv')

con1 = df['백신 접종 횟수']>0
co1 = df['백신 접종 횟수'] == 0
print(con1.sum(),co1.sum())

con2 = (df['연령']>=65)&(df['백신 접종 횟수']>0)&(df['양성 여부']==1)
print(df[con2])