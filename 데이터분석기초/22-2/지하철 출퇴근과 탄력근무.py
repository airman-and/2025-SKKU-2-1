import numpy as np
import pandas as pd

df = pd.read_csv('itsuka/subway_31_combined.csv')
complex = []


# 노선 혼잡도
a,b = map(int,input().split())
count = [x for x in range(a, b+1)]

for i in range(a-4,b+1-4):
    complex.append(df.iloc[:,2*i-1].sum()+df.iloc[:,2*i].sum())

print(complex)
# complex는 크기 count는 시간대

tax = min(complex)
idx = complex.index(tax)
print(count[idx])






