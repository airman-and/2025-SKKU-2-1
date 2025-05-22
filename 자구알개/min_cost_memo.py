M = 3
N = 4
cache = [[0] * N for i in range(0,M)]

def get_min(a, b):
    return a if a < b else b

def min_cost_memo(mat, i, j):
    if cache[i][j] != 0:
        return cache[i][j]
    if i == 0 and j == 0:
        cache[i][j] = mat[i][j]
        return cache[i][j]
    if i == 0:
        cache[i][j] = mat[i][j] + min_cost_memo(mat, i, j-1)
        return cache[i][j]
    if j == 0:
        cache[i][j] = mat[i][j] + min_cost_memo(mat, i-1, j)
        return cache[i][j]
    else:
        a = min_cost_memo(mat, i-1, j)
        b = min_cost_memo(mat, i, j-1)
        cache[i][j] = mat[i][j] + get_min(a, b)
    return cache[i][j]
mat = [[1, 3, 5, 8],
       [4, 2, 1, 7],
       [4, 3, 2, 3]]
print(min_cost_memo(mat, M-1, N-1))
# Output: 12
