import random

num_loops = 10000
max_num = 1000
nums_list = []

for i in range(num_loops):
    RN = random.randint(0, max_num)
    notFound = True
    for j in range(len(nums_list)):
        if RN == nums_list[j][0]:  # RN 값이 이미 존재하는지 확인
            nums_list[j][1] += 1
            notFound = False
            break
    if notFound:  # 첫 출현이라면 [RN, 1] 형태로 추가
        nums_list.append([RN, 1])
print(nums_list)