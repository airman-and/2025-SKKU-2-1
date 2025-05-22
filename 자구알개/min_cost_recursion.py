M =3
N =4

def get_min(a, b):
    return a if a < b else b

def min_cost_recursion(cost, m, n):
    if m == 0 and n == 0:
        return mat[0][0]
    if m == 0:
        return mat[0][n] + min_cost_recursion(cost, 0, n-1)
    if n == 0:
        return mat[m][0] + min_cost_recursion(cost, m-1, 0)
    a = min_cost_recursion(cost, m-1, n)
    b = min_cost_recursion(cost, m, n-1)
    return mat[m][n] + get_min(a, b)

mat = [[1, 3, 5, 8],
       [4, 2, 1, 7],
       [4, 3, 2, 3]]
print(min_cost_recursion(mat, M-1, N-1))
# Output: 12