price_tag = {'아메리카노': 2500, '카페라떼':3000,'에스프레소':2000,'티':2200,'케이크':4500}
menu_list = list(price_tag.keys())
# 어떤 리스트를 만들어야할까?
sell = [0]*5 # 리스트의 크기를 배정해주어야한다.
total = 0

while True:
    menu,num = map(int, input().split())
    if menu == 0 and num == 0:
        break
    sell[menu-1] += num

print(f"""
판매 내역:
아메리카노: {sell[0]}개
카페라떼: {sell[1]}개
에스프레소: {sell[2]}개
티: {sell[3]}개
케이크: {sell[4]}개
""")
    
for i in  len(sell):
    total = price_tag[i]*list[i]
print(f'총 매출: {total}원')

max_index = sell.index(max(sell))

print(f'가장 인기 메뉴: {menu_list[max_index]}')





