# Programming Assignment - 2: The power of 2
n = int(input())

def func(n):
  if n == 2:
    print("YES",end="")
  elif n < 2:
    print("NO",end="")
  else:
    func(n/2)

func(n)
    