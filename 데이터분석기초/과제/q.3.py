# 따로 csv를 불러오는 것이 아니라 price_dict와 sold_dict에 자동으로 저장되어 있습니다.
# 31개의 데이터를 다 나타내기 어려워 csv파일을 통해 제공된다는 점 참고바랍니다.
# 과일 가격은 사과, 수박, 딸기, 참외, 포도, 멜론, 바나나, 망고, 키위, 파인애플 순서로 주어집니다.

# 각 날짜별 과일 가격 정보 (예시)
price_dict = {
    '1': [1000, 2500, 2000, 2300, 4000, 1200, 4200, 2100, 3000, 2000],
    '2': [1400,	3600,	2700,	2700,	4600,	5700,	1300,	4900,	3800,	5900],
		'3': [1600,	2700,	2100,	3200,	3700,	4000,	1200,	3900,	1700,	5700],
    # ... 31일까지 데이터가 있다고 가정  
}

# 각 날짜별 판매된 과일 정보 (예시)
sold_dict = {
    '1': ['수박', '참외', '딸기', '딸기', '딸기', '수박', '참외'],
    '2': ['사과', '멜론', '포도', '키위', '파인애플', '포도', '망고', '망고', '딸기', '멜론', '포도', '망고', '포도', '포도', '망고'],
		'3': ['키위', '멜론', '포도', '바나나', '파인애플', '딸기', '바나나', '포도', '멜론', '참외', '수박', '바나나'],
    # ... 31일까지 데이터가 있다고 가정
}

# 입력은 아래의 input() 함수를 통해 이루어지므로, 별도의 입력 코드를 작성할 필요가 없습니다.
# 입력하는 과일 fruit_name 저장
fruit_name = input()
import pandas as pd

df_price = pd.read_csv("data/Q3_price_data.csv")
df_sold = pd.read_csv("data/Q3_sold_data.csv")

# 데이터 딕셔너리 변환
price_dict = {
    str(row["날짜"]): row.drop("날짜").tolist()
    for _, row in df_price.iterrows()
}

sold_dict = {
    str(row["날짜"]): row["판매된 과일"].split(", ")
    for _, row in df_sold.iterrows()
}

# 변수 선언과 모듈 설정 변수 선언과 모듈 설정
from collections import Counter
import csv
number= 0
total_revenue=0
sum=0
a=[]
A=[]
b=[]
B=[]
result=[]
ordered_fruits = ['사과', '수박', '딸기', '참외', '포도', '멜론', '바나나', '망고','키위','파인애플']
total_sales=0
with open("data/Q3_price_data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader, None)
    data1 = list(reader)  
	# 가격을 이중 리스트로 만들었다.
with open("data/Q3_sold_data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f) 
    next(reader, None)
    data2 =list(reader)

#과일 종류 정하기
number = ordered_fruits.index(fruit_name)

#리스트 정제 과정
for i in range(31):
	a= data1[i]
	a.remove(str(i+1))
	A.append(a)	
#리스트 정제 과정 B의 원소들이 제대로 구분되지 않는 문제가 발생
for i in range(31):
	b= data2[i]
	b.remove(str(i+1))
	B.append(b)

for row in B:
    fruits = [fruit.strip() for fruit in row[0].split(',') if fruit.strip()]
    counts = Counter(fruits)
    
    result.append([counts.get(fruit, 0) for fruit in ordered_fruits])

for i in range(31):
	total_revenue  = total_revenue+int(A[i][number])*int(result[i][number])
	






# 출력은 아래의 print() 함수를 통해 이루어지므로, 별도의 출력 코드를 작성할 필요가 없습니다.
# 입력된 과일의 총 수익을 저장하고 있는 total_revenue 출력  
print(int(total_revenue))