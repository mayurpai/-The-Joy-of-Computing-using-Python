# Programming Assignment 3: Function and Dictionary
def printDict():
    result = {}
    n = int(input())
    for i in range(1,n+1):
  	    result[i] = i*i
    print(result,end="")
printDict()