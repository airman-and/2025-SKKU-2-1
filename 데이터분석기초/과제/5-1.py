# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

numbers = list(map(int, input().split()))  # This will give you List of Integers
# Write your own code!
num = set(numbers)
num_of_unique_nums = len(num)

print(num_of_unique_nums)

#map을 이용해서 전체 리스트 요소에 int라는 함수를 적용하는 것이다. map(함수, 객체)
