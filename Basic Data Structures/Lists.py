#Lists are used to store a set of values .  lists are mutable in nature 

fruits = ["Apple" , 123,1.5,False ,"Banana" , "Grapes","Mango"]
fruits[1] = "Pineapple"
print(fruits)
print(fruits[1:4]) #prints from index 1 to 4

fruits.append("Orange") #append is used to add a value at the end of the list
print(fruits)

l1 = [1,4,6,3,8,3]
l1.reverse() # reverse the list
print(l1)
l1.sort() # sort the list
print(l1)

l1.insert(3,100) # insert 100 at index 3
print(l1)

print(l1.pop(0)) # pop the value at index 0 and print it
# pop is used to remove a value from the list
l1.remove(8)
print(l1)

#----------------------------------------------------------------------
# input 5 names of students and store them in a list

st = []
for i in range(5):
    name = input("Enter the name of student: ")
    st.append(name)

print(st)

#----------------------------------------------------------------------
# while loop
#---------------------------------------------------------------------
# count number of digits in a number using while loop given number is n
n = int(input("Enter the number: "))
count = 0
while n != 0:
    count += 1
    n = n // 10
    print(count)
