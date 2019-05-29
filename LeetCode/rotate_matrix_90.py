def rotate(A):
    n = len(A)
    # Transpose the matrix
    for i in range(n):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    
    # Flip Horizontally
    for row in A:
        for j in range(n//2):
            row[j], row[~j] = row[~j], row[j]
    print(A)

mat = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

rotate(mat)
print(mat)