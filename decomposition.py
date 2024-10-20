import numpy as np

def decomposition(A):
  n = len(A)

  L = [[0 for row in range(n)] for col in range(n)]
  U = [[0 for row in range(n)] for col in range(n)]

  for p in range(n):
    for j in range(p, n):
      sum = 0
      for k in range(p):
        sum = sum + L[p][k] * U[k][j]
      U[p][j] = A[p][j] - sum

    q = p
    for i in range(q, n):
      if i == q:
        L[i][q] = 1
      else:
        sum = 0
        for k in range(q):
          sum = sum + L[i][k] * U[k][q]
        L[i][q] = (A[i][q] - sum) / U[q][q]

  return L, U

def forward_subs(b, L):
  n = len(b)
  t = [0] * n

  for i in range(n):
    sum = 0
    for j in range(i):
      sum = sum + L[i][j] * t[j]
    t[i] = b[i] - sum

  return t

def backward_subs(t, U):
  n = len(t)
  x = [0] * n

  for i in range(n, 0, -1):
    sum = 0
    for j in range(i, n):
      sum = sum + U[i-1][j] * x[j]
    x[i-1] = (1 / U[i-1][i-1]) * (t[i-1] - sum)

  return x

def solve_LU(A, b):
  L, U = decomposition(A)

  t = forward_subs(b, L)

  x = backward_subs(t, U)

  return x

def show(matrix):
  n = len(matrix)
  for row in range(n):
    for col in range(n):
      print('%.2f' % matrix[row][col], end="\t")
    print("")

n = int(input("Ukuran matrix A: "))
A = []
for i in range(n):
  row = []
  for j in range(n):
    element = float(input(f"Masukan A[{i+1}][{j+1}]: "))
    row.append(element)
  A.append(row)

b = []
for i in range(n):
  element = float(input(f"Masukan b[{i+1}]: "))
  b.append(element)

x = solve_LU(A, b)

for i in range(len(x)):
  print(f'x_{i+1} : {x[i]:.2f}')

L, U = decomposition(A)

print("Matrix L:")
show(L)

print("\nMatrix U:")
show(U)

LU = np.dot(L, U)
print("\nL.U:")
show(LU)
