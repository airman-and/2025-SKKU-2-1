# 따로 csv를 불러오는 것이 아니라 price_dict와 sold_dict에 자동으로 저장되어 있습니다.
# 31개의 데이터를 다 나타내기 어려워 csv파일을 통해 제공된다는 점 참고바랍니다.
# 과일 가격은 사과, 수박, 딸기, 참외 순서로 주어집니다.
# 1일은 월요일이며 31일까지 있습니다.

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
# 입력되는 요일은 월요일, 화요일, 수요일, 목요일, 금요일, 토요일, 일요일 중 하나입니다.
# 입력하는 요일을 input_day에 저장됩니다.
input_day = input()
# 예시) 입력 : 월요일 -> 1일, 8일, 15일, 22일, 29일의 모든 매출의 합 및 가장 매출액이 높은 과일 출력
import pandas as pd

df_price = pd.read_csv("data/Q4_price_data.csv")
df_sold = pd.read_csv("data/Q4_sold_data.csv")

# 데이터 딕셔너리 변환
price_dict = {
    str(row["날짜"]): [row["사과 가격"], row["수박 가격"], row["딸기 가격"], row["참외 가격"]]
    for _, row in df_price.iterrows()
}

sold_dict = {
    str(row["날짜"]): row["판매된 과일"].split(", ")
    for _, row in df_sold.iterrows()
}
# 모듈과 변수와 함수 선언!
from collections import Counter
import csv

#요일에 맞는 날짜를 뽑아올 함수 생성
def get_dates_by_weekday(total_days: int, start_weekday: str, target_weekday: str) -> list[int]:
    weekdays = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
    start_idx = weekdays.index(start_weekday)
    target_idx = weekdays.index(target_weekday)

    return [
        day
        for day in range(1, total_days + 1)
        if (start_idx + day - 1) % 7 == target_idx
    ]
ordered_fruits = ['사과', '수박', '딸기', '참외']
result =[]
A = []
a=[]
ai=[]
B=[]
total_sales=0
most_sold_fruit=''
day = get_dates_by_weekday(31,'월요일', input_day)




# CSV파일 뽑아내기
with open("data/Q4_price_data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader, None)
    data1 = list(reader)  

with open("data/Q4_sold_data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f) 
    next(reader, None)
    data2 = list(reader)


# 날짜에 맞는 리스트만 뽑아오기
for k in data1:
	for i in day:
			if i == int(k[0]):
				A.append(k)

for sub in A:
    if sub:
        sub.pop(0)

# 날짜에 맞는 리스트만 뽑아오기2

for k in data2:
	for i in day:
			if i == int(k[0]):
				B.append(k)
for sub in B:
    if sub:
        sub.pop(0)

			
for row in B:
    fruits = [fruit.strip() for fruit in row[0].split(',') if fruit.strip()]
    counts = Counter(fruits)
    
    result.append([counts.get(fruit, 0) for fruit in ordered_fruits])



total_sales = sum(
    int(price) * qty
    for price_row, qty_row in zip(A, result)
    for price, qty in zip(price_row, qty_row)
)



revenues = [ sum(int(p)*q for p, q in zip(price_col, qty_col)) 
            for price_col, qty_col in zip(zip(*A), zip(*result)) ]
max_index = revenues.index(max(revenues))


most_sold_fruit=ordered_fruits[max_index]





















# 가장 많이 팔린 과일이 반드시 하나 존재하며, 판매 수량이 같은 경우는 없습니다
# 입력한 요일에 발생한 모든 매출의 합이 저장된 total_sales 변수를 출력합니다. 
# 입력한 요일에 가장 매출액이 높은 과일이 저장된 most_sold_fruit 변수를 출력합니다.
print(int(total_sales))
print(most_sold_fruit)