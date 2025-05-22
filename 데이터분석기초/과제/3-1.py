# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())  # 사용자 입력 받기
i = 1  # i 초기화

while i <= 9:  # 1부터 9까지 반복
    print(f"{N} * {i} = {N * i}")  # 가독성을 위해 공백 추가
    i += 1  # i 증가
# 지금 까지 배운 것의 집합으로써 f"{N} * {i} = {N * i}" 이것을 작성할 수 있었고
# += -= 를 이용할 수 있었다.*= /= %= 와 같은 연산자도 있다.