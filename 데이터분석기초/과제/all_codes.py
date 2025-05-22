# ==== File: 22-2/간식비 정산.py ====
import numpy as np
import pandas as pd

expenses = np.array([
    20000, 17000, 15000, 22000, 12000, 18000, 21000,   # 1주차 (월~일)
    10000,  8000, 15000, 14000, 16000, 19000, 17000,   # 2주차
    21000, 18000, 12000, 13000, 11000, 15000, 16000,   # 3주차
    19000, 17000, 18000, 14000, 13000, 15000, 20000    # 4주차
])
ex=expenses.reshape(4,7)

요일 = ['월','화','수','목','금','토','일']

ex = pd.DataFrame(ex,columns = 요일)
a= input()
e=ex[a].sum()
print(e)




# ==== File: 22-2/소비 습관 2.py ====
import pandas as pd
import numpy as np

df = pd.read_csv('jurk\입출금.csv')

# 카테고리 별 총 출금 내역을 특정 기준으로 출력한다.
# 출금 및 카테고리 열을 제외한 나머지 열을 제거
# 카테고리 별 총 출금량을 계산하여, 출금량이 많은 카테고리부터 순서대로 정렬한다.
#총 출금량이 0인 카테고리 또한 제거한다.
#결과물을 out 변수에 저장한다.

df = df.drop(columns=['일시', '입금', '잔고'])
gb = df.groupby('카테고리')
ggb = gb.sum()



out = ggb.sort_values(by = '출금',ascending=False)
print(out)
print(np.array(out.values).flatten())


# ==== File: 22-2/소비습관1.py ====
import pandas as pd

# 1) 예시 데이터프레임 생성
df = pd.DataFrame({
    '일시': ['2025-04-01', '2025-04-02', '2025-04-03', '2025-04-04', '2025-04-05'],
    '카테고리': ['교통비',   '식비',     '교통비',   '문화비',   '교통비'],
    '입금':   [0,         100000,     0,         50000,     0],
    '출금':   [5000,      0,          1,      0,         7000],
    '잔고':   [945000,    1045000,    1042000,   1092000,   1095000]
})

# 2) 원하는 카테고리 지정
category = input()

# 3) 해당 카테고리 & 출금이 0이 아닌 행 필터링 후 내림차순 정렬
mask = (df['카테고리'] == category) & (df['출금'] != 0)

out = df.loc[mask, '출금'].sort_values(ascending = False)

# mask = (df['카테고리]==category) & (df['출금'] !=0)


# 4) 결과 출력
print("원본 데이터프레임:")
print(df)
print("\n카테고리 =", category, "출금 내역 (내림차순):")
print(out)
print(f"\n최대 출금액: {out.iloc[0]}, 최소 출금액: {out.iloc[-1]}")




# ==== File: 22-2/어려운 문제.py ====
a,b,c = map(int,input().split())
count=0
score_0 = [82, 54, 2, 86, 76, 85, 33, 60, 57, 35]
score_1 = [72, 47, 66, 61, 98, 78, 47, 52, 83, 98]
score_2 = [20, 52, 59, 67, 74, 81, 47, 56, 89, 98]


for i,j,k in zip(score_0,score_1,score_2):
    if i>a and j>b and k>c:
        count += 1
print(count)

# ==== File: 22-2/지하철 출퇴근과 탄력근무.py ====
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








# ==== File: 22-2/지하철.py ====
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





# ==== File: 22-2/축하 파티 음료수 돌리기.py ====
from collections import defaultdict
from collections import defaultdict
#위 모듈을 이용하면 0으로 채워져 있는 dict를 만들 수 있다?라고 보면 될듯?
#이는 아주 손 쉽게 이름:숫자 를 추가할 수 있다는 것이다.
drink_dict = {
    "강민": "콜라",
    "홍진호": "콜라",
    "임요환": "카페라떼",
    "민명숙": "카라멜마끼아또"
}

order = []
print("프로세스가 시작되었습니다. (입력값을 직접 입력해 주세요)")
while True:
    name = input()
    if name == "종료":
        break
    order.append(name)

drink_count = defaultdict(int)
unknown_count = 0

for name in order:
    if name in drink_dict:
        drink_count[drink_dict[name]] += 1
    else:
        unknown_count += 1

for drink, count in drink_count.items():
    print(f"{drink} {count}잔")
if unknown_count > 0:
    print(f"취향을 모르는 사람 {unknown_count}명")
print("프로세스가 종료되었습니다.")

     
     

    


# ==== File: 22도전/1.py ====
jum = 0
lis = []

while True:
    jum = int(input())
    if jum == -1:
        break
    elif jum >= 70:
        lis.append('A')
    elif jum >= 50:
        lis.append('B')
    elif jum >= 25:
        lis.append('C')
    elif jum < 25:
        lis.append('D')
for i in lis:
    print(i)
    

# ==== File: 22도전/2.py ====
temp = {   '추움':'코트',
    '따듯함':'점퍼',
    '더움':'티셔츠',

}
out = {
    '회의':'구두',
    '운동':'운동화',
    '슈퍼':'슬리퍼'
}
spe = {
    '황사':'마스크',
    '햇빛':'선글라스',
    '우천':'우산'
}

a = input('날씨는 어떻습니까?')
b = input('어디에 가십니까?')
c = input('특수 상황은 무엇입니까?')

print(f'{temp[a]} 를 입고, {out[b]} 를 신고, {spe[c]} 를 챙기세요.')


# ==== File: 22도전/3.py ====
import pandas as pd

df = pd.read_csv('C:\\Users\\andycho\\OneDrive\\Desktop\\2025 2학년 1학기\\22도전\\vaccine_data_500.csv')

con1 = df['백신 접종 횟수']>0
co1 = df['백신 접종 횟수'] == 0
print(con1.sum(),co1.sum())

con2 = (df['연령']>=65)&(df['백신 접종 횟수']>0)&(df['양성 여부']==1)
print(df[con2])

# ==== File: 22도전/4.py ====
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






    


# ==== File: 22도전/5.py ====
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

    


# ==== File: 22도전/6.py ====
import pandas as pd

df = pd.read_csv(
    r'C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\22도전\transactions.csv'
)

# 할부 결제인 행만 필터링 (할부개월수 > 0)
df_inst = df[df['할부개월수'] > 0]

# 상호명별 할부 결제 횟수 집계
counts = df_inst['상호명'].value_counts()

# 최댓값을 가지는 상호명 추출
top = counts.idxmax()
print(f"1년간 할부 결제 횟수가 가장 많은 가맹점: {top}")









# ==== File: 22도전/7.py ====
import pandas as pd

# 파일 경로
path_m = r'C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\22도전\merchants.csv'
path_p = r'C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\22도전\payments.csv'

# CSV 읽기 (BOM 포함 UTF-8)
merchants = pd.read_csv(path_m, encoding='utf-8-sig')
payments  = pd.read_csv(path_p, encoding='utf-8-sig')

# 병합 및 분기 계산
df = payments.merge(merchants, on='상호명')
df['month']   = df['결제월'].str.rstrip('월').astype(int)
df['quarter'] = ((df['month'] - 1) // 3) + 1

# 분기·업종별 합계 구하고, 분기별 최댓값만 추출
agg = df.groupby(['quarter','업종'], as_index=False)['결제금액'].sum()
top = agg.loc[agg.groupby('quarter')['결제금액'].idxmax()]

# 출력
for _, r in top.sort_values('quarter').iterrows():
    print(f"{int(r['quarter'])}분기: {r['업종']}")


