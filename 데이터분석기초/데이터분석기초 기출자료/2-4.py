height = float(input())
weight = float(input())
BMI = weight/(height**2)

if(BMI<18.5):
	print("저체중")
elif(BMI<23):
	print("정상")
elif(BMI<25):
	print("과체중")
elif(BMI<30):
	print("경도비만")
elif(BMI<35):
	print("중도비만")
else:
	print("고도비만")
 
 # if문을 중첩으로 쌓는 방법을 배우고 또한 **(제곱연산자), /(나누기 연산자에 