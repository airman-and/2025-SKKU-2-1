a = []
b=0
while True:
    b = int(input())
    if b == -1:
         break
    a.append(b)
average = sum(a) / len(a)
print(f"{average:.2f}")