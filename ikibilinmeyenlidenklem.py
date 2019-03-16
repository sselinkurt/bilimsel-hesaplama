a1, b1, c1 = 1, 2, 1
a2, b2, c2 = 3, 4, -2

A = [[a1, b1, c1], [a2, b2, c2]]

k=1
for t in range(0, 2):
    if(t==1):
        k=0
    for i in range(2, -k, -1):
        A[k][i] = -A[k][t]/A[t][t]*A[t][i]+A[k][i]
     
print((A[0][2]/A[0][0]),(A[1][2]/A[1][1]))

