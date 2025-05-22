jum = 0
lis = []

while True:
    jum = int(input())
    if jum == -1:
        break
    elif jum >= 70:
        lis.append('A')
    elif jum >= 50:
        lis.append('B')
    elif jum >= 25:
        lis.append('C')
    elif jum < 25:
        lis.append('D')
for i in lis:
    print(i)
    