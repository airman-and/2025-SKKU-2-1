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

     
     

    
