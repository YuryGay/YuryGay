n = int(input())
mat = [['.' for _ in range(n)] for _ in range(n)]
s = (n - 1) / 2
for i in range(n):
    for j in range(n):
        if i == j or i == n - 1 - j or i == s or j == s:
            mat[j][i] = '*'
        print(mat[j][i], end = ' ')
    print()
