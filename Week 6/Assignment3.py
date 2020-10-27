# Programming Assignment 3: Lower Triangular Matrix
n=int(input())
matrix=[]
for i in range(n):
    for j in range(1):
        ele=[int(a) for a in input().split()]
        matrix.append(ele)


for i in range(n):
    for j in range(n):
        if i<j:
            if j==n-1:
                print(0,end="")
            else:
                print(0,end=" ")
        else:
            if j==n-1:
                print(matrix[i][j],end="")
            else:
                print(matrix[i][j],end=" ")
        
    if i!=n-1:
      print()