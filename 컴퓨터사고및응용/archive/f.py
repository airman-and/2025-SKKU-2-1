import math

R = int(input("원의 반지름: "))
if(R>=0):
    print(f"원의 면적: {math.pi*R**2}")
else:
    print(" 잘못된 값입니다")

a,b,c = map(int(input("3개의 정수를 입력하시오: ")))
