def linear_search(lst, n, x):
    for i in range(n):
        if lst[i] == x:
            return i
    return -1

lst = [10, 7, 11, 5, 3, 8, 16, 13]
n = len(lst)
result = linear_search(lst, n, 10)
if result != -1:
    print("Found at index {}".format(result))
else:
    print("Not found.")
    
    