import pandas as pd

df = pd.read_csv('22도전\sales_12months_31days.csv')
lis = []
li = []
l = []
a = 0
b = 0
c = 0
c1 = 0
c2 = 0

for i in range(1,5):
    lis.append(df.iloc[:,i].sum())
    a = max(lis)
    b = lis.index(a)
    c = b+1

for i in range(5,8):
    li.append(df.iloc[:,i].sum())
    a = max(li)
    b = li.index(a)
    c1 = b+5

for i in range(8,11):
    l.append(df.iloc[:,i].sum())
    a = max(l)
    b = l.index(a)
    c2 = b+8
    

print(df.columns[c],df.columns[c1],df.columns[c2])

    
