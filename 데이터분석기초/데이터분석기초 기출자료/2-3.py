leapyear = int(input())
if (leapyear % 400 == 0) or (leapyear % 4 == 0 and leapyear % 100 != 0):
    print("True")
else:
    print("False")
# leapyear는 윤년으로 if문과 else문을 사용하여 윤년인지 아닌지를 판단한다.
# 




