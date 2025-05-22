def get_min(a, b):
    return a if a < b else b

def coin_change(demo, n):
    k = len(demo)
    cache = [[0] * (n+1) for i in range(0, k)]
    for i in range(0, k):
        cache[i][0] = 0
    for j in range(1, n+1):
        cache[0][j] = j 
    
    for i in range(1, k):
        for j in range(1, n+1):
            if demo[i] > j:
                cache[i][j] = cache[i-1][j]
            else:
                cache[i][j] = get_min(cache[i-1][j], cache[i][j-demo[i]] + 1)
    print_coin_change(demo, cache, n)
    return cache[k-1][n]

def print_coin_change(demo, cache, n):
    i = len(demo) - 1
    j = n
    while j != 0:
        if cache[i - 1][j] == cache[i][j] and i > 0:
            i -= 1
        else:
            print(demo[i], end=" ")
            j -= demo[i]

demo = [1, 5, 10, 12, 50, 100, 500]
n = 16
coin_change(demo, n)
# Output: 1 5 10