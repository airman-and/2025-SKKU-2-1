def coin_change(x):
    d = [1,5,10,50,100,500]
    result = []
    i = len(d)-1
    while True:
        while x >= d[i]:
            x = x-d[i]
            result.append(d[i])
        i -= 1
        if i < 0:
            break
    for i in range(len(result)):
        print(result[i], end=' ')
x=16
coin_change(x)