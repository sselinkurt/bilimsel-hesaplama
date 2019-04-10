a1, b1, c1 = 1, 2, 1
a2, b2, c2 = 3, 4, -2
A = [[a1, b1, c1], [a2, b2, c2]]


A = [[-A[j%2][i]*A[(j+1)%2][j%2]/A[j%2][j%2]+A[(j+1)%2][i] for i in range(3)] for j in range(2)]

print(A[1][2]/A[1][0], A[0][2]/A[0][1])
