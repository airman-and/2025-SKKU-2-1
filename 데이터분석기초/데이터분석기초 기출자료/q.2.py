# 따로 csv를 불러오는 것이 아니라 price_dict와 sold_dict에 자동으로 저장되어 있습니다.
# 31개의 데이터를 다 나타내기 어려워 csv파일을 통해 제공된다는 점 참고바랍니다.
# 과일 가격은 사과, 수박, 딸기, 참외 순서로 주어집니다.

# 각 날짜별 과일 가격 정보 (예시)
price_dict = {
    '1': [1000, 2500, 2000, 2300],
    '2': [1500, 2000, 2200, 1800],
		'3': [2000, 1900, 2100, 1900],
    # ... 31일까지 데이터가 있다고 가정  
}

# 각 날짜별 판매된 과일 정보 (예시)
sold_dict = {
    '1': ['수박', '참외', '딸기', '딸기', '딸기', '수박', '참외',],
    '2': ['수박', '딸기', '수박', '참외', '수박', '딸기', '수박', '수박', '딸기', '수박', '참외', '참외'],
		'3': ['참외', '딸기', '수박', '딸기', '참외', '참외', '수박', '딸기', '수박', '수박'],
    # ... 31일까지 데이터가 있다고 가정
}

# 입력은 아래의 input() 함수를 통해 이루어지므로, 별도의 입력 코드를 작성할 필요가 없습니다.
# 입력하는 날짜를 input_date에 저장
input_date = input()
import pandas as pd

df_price = pd.read_csv("data/Q2_price_data.csv")
df_sold = pd.read_csv("data/Q2_sold_data.csv")

# 데이터 딕셔너리 변환
price_dict = {
    str(row["날짜"]): [row["사과 가격"], row["수박 가격"], row["딸기 가격"], row["참외 가격"]]
    for _, row in df_price.iterrows()
}

sold_dict = {
    str(row["날짜"]): row["판매된 과일"].split(", ")
    for _, row in df_sold.iterrows()
}
import csv
a=[]
b=[]
result=[]
total_sales=0
# 기본적인 선언문
with open("data/Q2_price_data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader, None)
    data1 = list(reader)  
	# 가격을 이중 리스트로 만들었따.
with open("data/Q2_sold_data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f) 
    next(reader, None)
    data2 = list(reader)  
	# 이중 리스트로 만든다.


for i in range(31):
	if input_date == data1[i][0]:
		a= data1[i]
		a.remove(str(i+1))
	#a라는 것을 만든 뒤 여기서 i
for i in range(31):
	if input_date == data2[i][0]:
		b= data2[i]
		b.remove(str(i+1))
if len(b) == 1:
    b = b[0].split(',')
clean_fruits = [fruit.strip() for fruit in b]

  

from collections import Counter


fruit_counter = Counter(clean_fruits)
ordered_fruits = ['사과', '수박', '딸기', '참외']
result = [fruit_counter[fruit] for fruit in ordered_fruits]




prices = [int(price) for price in a]
sales = [price * count for price, count in zip(prices, result)]
total_sales = sum(sales)





#지금 내가 하려는게 i로 1~31까지 찾아본 뒤 k를 이용해서 data1을 분석한다.

        


# 출력은 아래의 print() 함수를 통해 이루어지므로, 별도의 출력 코드를 작성할 필요가 없습니다.
# 입력된 날짜의 총 매출 값을 저장하고 있는 total_sales 출력  
print(int(total_sales))