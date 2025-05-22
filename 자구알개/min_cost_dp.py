M = 3
N = 4

def get_min(a, b):
    return a if a < b else b

def min_cost_dp(mat, i, j):
    cache = [[0] * N for i in range(0,M)]
    cache[0][0] = mat[0][0]
    for j in range(1, N):
        cache[0][j] = cache[0][j-1] + mat[0][j]
    for i in range(1, M):
        cache[i][0] = cache[i-1][0] + mat[i][0]
    for i in range(1, M):
        for j in range(1, N):
            cache[i][j] = mat[i][j] + get_min(cache[i-1][j], cache[i][j-1])
    return cache[M-1][N-1]
mat = [[1, 3, 5, 8],
       [4, 2, 1, 7],
       [4, 3, 2, 3]]
print(min_cost_dp(mat, M-1, N-1))
# Output: 12

