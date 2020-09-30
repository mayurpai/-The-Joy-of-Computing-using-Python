# Programming Assignment 3 : Divisibility
list_1 = []
for i in range(1,51):
	list_1.append(i)
a = int(input())
count = 0
for item in list_1:
	if item % a == 0 and item != a:
	    count+=1
print(count,end='')
