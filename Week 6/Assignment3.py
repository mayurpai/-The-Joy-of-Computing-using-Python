# Programming Assignment 3: Lower Triangular Matrix
matrix = []
n = int(input())
for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)

for i in range(n):
    for j in range(n):
        if i<j:
            matrix[i][j] = 0
            
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print()