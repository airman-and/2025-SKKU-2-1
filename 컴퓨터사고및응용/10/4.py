import csv

f = open(r"C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\컴퓨터사고및응용\10\weather.csv", 'r', encoding='utf-8')
data = csv.reader(f)
header = next(data)
min_temp = 1000
min_date = ""

for row in data:
    try:
        if len(row) >= 4 and row[3].strip():  # 데이터가 있고 비어있지 않은지 확인
            current_temp = float(row[3])
            if min_temp > current_temp:
                min_temp = current_temp
                min_date = row[0]
    except (ValueError, IndexError) as e:
        continue

if min_date:  # 데이터를 찾았을 경우에만 출력
    print(f'가장 추웠던 날은 {min_date}로, 기온은 {min_temp}도 입니다.')
else:
    print('유효한 데이터를 찾을 수 없습니다.')

f.close()
