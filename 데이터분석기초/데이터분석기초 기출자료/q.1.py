# 입력은 아래의 input() 함수를 통해 이루어지므로, 별도의 입력 코드를 작성할 필요가 없습니다.
# 입력하는 과일 판매 목록이 리스트형태로 변환되어 sold_fruits_list 변수에 저장됩니다.
sold_fruits_list = [fruit.strip() for fruit in input().split(",")]
# 예시) 입력 : 사과, 수박, 딸기, 딸기  ->  sold_fruits_list=['사과', '수박', '딸기', '딸기']
fruit_type = list(set(sold_fruits_list))

zero_list = [0] * len(fruit_type)

fruit_dict = dict(zip(fruit_type, zero_list))

for i in sold_fruits_list:
	for k in fruit_dict:
		if i==k:
			fruit_dict[k] += 1
max_key = max(fruit_dict, key=fruit_dict.get)
best_selling_fruit = max_key



# 출력은 아래의 print() 함수를 통해 이루어지므로, 별도의 출력 코드를 작성할 필요가 없습니다.
# 판매된 개수가 가장 많은 과일이 저장된 best_selling_fruit 변수를 출력
print(best_selling_fruit)