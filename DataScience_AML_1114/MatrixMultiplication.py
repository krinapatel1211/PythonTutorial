A = [
    [10, 11, 12],
     [12, 14, 15],
     [16, 17, 18]
]
B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(j)):
            



print(A[0][0]*B[0][0]+A[0][1]*B[1][0]+A[0][2]*B[2][0])
print(A[0][0]*B[0][1]+A[0][1]*B[1][1]+A[0][2]*B[2][1])
print(A[0][0]*B[0][2]+A[0][1]*B[1][2]+A[0][2]*B[2][2])