count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

L = []

while True:
    K = input()
    if K == "0":
        break
    if K in count:
        count[K] += 1

    L.append(count[K])

for i in range(len(L)):
    print(L[i])


#a라고 입력할때마다 증가하는 것이 아닌 것 같다.출력과 입력이 따로 놀 수는 없을까?