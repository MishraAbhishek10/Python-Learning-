myList = [1,2,3,4,5]

sqList = []

for it in myList:
    sqList.append(it*it)
print(sqList)

# now using comprehension it can be done in one line 
cuList = []
cuList = [it*it*it for it in myList]
print(cuList)

