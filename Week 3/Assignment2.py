# Programming Assignment 2 : List Slicing
a, b = input().split()
a = int(a)
b = int(b)
list_1 = []
for i in range(1,51):
	list_1.append(i)
for item in list_1[a:b]:
    print(item)
