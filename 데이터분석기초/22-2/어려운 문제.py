a,b,c = map(int,input().split())
count=0
score_0 = [82, 54, 2, 86, 76, 85, 33, 60, 57, 35]
score_1 = [72, 47, 66, 61, 98, 78, 47, 52, 83, 98]
score_2 = [20, 52, 59, 67, 74, 81, 47, 56, 89, 98]


for i,j,k in zip(score_0,score_1,score_2):
    if i>a and j>b and k>c:
        count += 1
print(count)