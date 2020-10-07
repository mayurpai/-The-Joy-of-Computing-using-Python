r,c = input().split()
r = int(r)
c = int(c)
count = 1
for i in range(r):
	for i in range(c):
		if r>0 and c==1:
			if i==r-1:
				print(count,end="")
			else:
				print(count,end="\n")
		elif i==c-1:
			print(count,end="\n")
		else:
			print(count,end=" ")
		count+=1
