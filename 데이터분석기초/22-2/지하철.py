import numpy as np
import pandas as pd

df = pd.read_csv('itsuka/subway_31_combined.csv')
complex = []
a,b,c = map(int,input().split())
count = [x for x in range(a, b+1)]
cpl =[]


for i in range(a-4,b-3):
    complex.append(df.iloc[:,2*i-1].sum()+df.iloc[:,2*i].sum())

for i in range(b-a+1-c-1):
    cpl.append(complex[i]+complex[i+c+1])

mi = min(cpl)
ind = cpl.index(mi)
haha = count[ind]
print(f'{haha} {haha+1} {haha+c+1}')



