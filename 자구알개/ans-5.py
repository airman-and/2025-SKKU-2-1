# 학번:2024315312        이름: 조현영

print("--- 1 ----")
# 음이 아닌 정수를 리스트로 나타낸다. 예: 1234는  [4, 3, 2, 1], 0은 [0]
# 이런 리스트 형태의 수로 변환하여 반환하는 함수 f를 
# 결과가 모두 True가 나오도록 '''''' 위치에 완성하시오.

def f(n):
    if n == 0:
        return[0]
    정수 = []
    while n > 0:
        정수.append(n%10)
        n//=10
        # 가장 작은 자리수의 숫자를 지속해서 append한 코드이다.
    return 정수

    
print(f(0) == [0])
print(f(45) == [5, 4])
print(f(12345) == [5, 4, 3, 2, 1])
print(f(123) == [3, 2, 1])



print("--- 2 ----")
# m부터 n까지의 덧셈식과 합을 문자열로 반환하는 함수 sum(m, n)을
# 결과가 모두 True로  나오도록 '''''' 위치에 작성하시오.
# 항의 수가 5 이상이면 중간에 ... 을 넣는다
# 예: 2+3+4+5=14,     2+3+...+7=27

def sum(m, n):
    전체합 = 0
    용어 = []
    for i in range(m,n+1):
        용어.append(i)
        전체합 += i
    개수 = n-m+1
    if 개수 < 5:
        k = '+'.join(str(x) for x in 용어) # 여기 join부분을 생각해내기가 가장 어려웠다. 이를 이용해서
        # 각각의 문자열 사이에 +를 삽입할 수 있었다.
    else:
        k = f"{m}+{m+1}+...+{n}"
    return f"{k}={전체합}"     



print(sum(2,5) == "2+3+4+5=14")
print(sum(2,7) == "2+3+...+7=27")
print(sum(5,100) == "5+6+...+100=5040")          


print("--- 3 ----")
# 함수 change(m, n500, n100)는 거스름 돈을 동전으로 지불한다.
# 동전으로는 500원, 100원이 있고 n500, n100은 각 동전이 있는 갯수이다.
# 500원 동전이 부족하면 100원 동전으로 지불해야 하고,
# 100원 동전이 있으면 최소한 하나는 지불해야 한다.
# 지불할 수 없으면 함수는 "NG"를 반환한다.
# 결과가 모두 True로  나오도록 '''''' 위치에 함수를 작성하시오.

def change(m, n500, n100):
    for i in range(n500,-1,-1):
        re=m-500*i # 500원을 사용했을 때 얼마나 남는지 확인해보는 것것
        if re < 0 or re % 100 != 0: #100원 단위로 맞지 않으면 건너뛴다. 이는 100원을 하나라도 사용하기 위함이다.
            continue
        k = re//100 # 남은 금액을 100원으로 해결가능한 개수수
        if k > n100: # 필요한 것의 개수가 실제 가진 개수보다 많을 때 
            continue
        if n100 > 0 and k<1: # 100원을 가지고 있는데 최소한 하나를 지불하지 않는 경우를 block
            continue
        return(i,k)
    return "NG"

print(change(500, 0, 10) == (0, 5))
print(change(500, 2, 10) == (0, 5))
print(change(500, 2, 0) == (1, 0))
print(change(1000, 2, 10) == (1, 5))
print(change(90, 1, 10) == "NG")
print(change(1000, 2, 4) == "NG")


print("--- 4 ----")
# 함수 exp(s)은 실수 형태인 문자열 "0.xxxx"을
# 매개변수 s로 받아 정수부분이 한자리인 지수 형태인 문자열로 반환한다.
# 결과가 모두 True 가 나오도록 '''''' 위치에 함수를 작성하시오..
# 참고로 문자열을 실수로 변환한 처리하면, 소숫점 이하가 일치하지 않을 수 있다.
# 따라서 처음부터 끝까지 문자열로 처리해야 한다.
# 힌트: 문자열에서 0이 아닌 숫자의 위치를 파악하여 지수를 결정해야한다.
#         "0.00123."은 소숫점을 3자리 옮겨야 되기때문에 지수가 -3이된다.

def exp(s):
    if '.' not in s: # .이 없으면 정수밖에 없으므로 원본값을 돌려준다.
        return f"bad: {s}"
    정수, 자리수 = s.split('.',1) # 그렇지 않으면 바로 분리리

    if 정수 != "0": # 정수가 0 인지 확인해줘야함함
        return f"bad: {s}"
    if not 자리수 or set(자리수) <= {'0'}: #비어 있냐 아니면 0으로만 적혀져 있냐냐
        return f"{s}e0"
    
    for i,j in enumerate(자리수):  # 인덱스 확인용도로 enumerate를 이용한다.
        if j != '0':
            처음 = i
            break
    
    지수 = -(처음 + 1)
    정수부분 = 자리수[처음]
    소수부분 = 자리수[처음+1:]
    return f"{정수부분}.{소수부분}e{지수}"

print(exp("0.001230") == "1.230e-3")
print(exp("0.10000") == "1.0000e-1")
print(exp("0.000") == "0.000e0")
print(exp("1234.") == "bad: 1234.")






