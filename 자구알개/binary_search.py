def binary_search(lst, n, x):
    mid = 0
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if x == lst[mid]:
            return mid
        if x < lst[mid]:
            high = mid -1
        else:
            low = mid + 1
        
    return -1

lst = [3,5,7,8,11,13,16]
n = len(lst)
result = binary_search(lst, n, 7)
if result != -1:
    print("Found at index {}".format(result))
else:
    print("Not found.")