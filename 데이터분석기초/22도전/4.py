import warnings
warnings.filterwarnings(action='ignore')
import pandas as pd
df = pd.read_csv('22도전\sales_12months.csv')

ma = 0
su = 0
lis = []


for i in range(120):
    su = df.iloc[i,1:].sum()
    lis.append(su)    

ma = max(lis)
su = lis.index(ma)
print(df.iloc[su,0])






    
