list_1 = []
n = int(input())
for i in range(n):
    list_1.append(int(input()))
list_1.sort()
for item in range(0,len(list_1)):
    if item==len(list_1)-1:
        print(list_1[item],end="")
    else:
        print(list_1[item],end=" ")
