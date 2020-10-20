# Programming Assignment - 1: Duplicate
input_string = input()

userList = input_string.split()
resultList = []

for i in userList:
  if i not in resultList:
    resultList.append(i)
  else:
    continue
for i in resultList:
    print(i,end=" ")