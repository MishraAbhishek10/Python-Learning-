'''
Tuple - Tuples are used to store multiple items in a single variable.
Tuples are ordered and immutable, meaning that once a tuple is created, it cannot be modified.
# tuple : immutable 
# list : mutable
#  tuple in Python can contain multiple data types within a single variable. 
# it allows duplicate values 
# Tuple is faster than list
# Tuple is more memory efficient than list
# Tuple is more suitable for large data sets
# Tuple is more suitable for data that is used in a loop,function,class,dictionary,set

'''

a = () # empty tuple 
b = (1, 2, 3, 4, 5,"Golu",123) # tuple with values 
print(type(a))

#how to make single valued tuple
c = (1,) # single valued tuple
d = (1)
print(type(c)) # output : tuple
print(type(d)) # output: int 

#-----------------------------------------------------------------------------------------
# Tuple Methods
#-----------------------------------------------------------------------------------------

# 1. count() : returns the number of occurrences of a specified value in the tuple.
# 2. index() : returns the index of the first occurrence of a specified value in th
t = (1,3,4,1,3,7,0,9)
print(t.count(1)) # output : 2
print(t.index(3)) # output : 1

#-----------------------------------------------------------------------------------------
tup = (1,2,3,4,5,6,7)
mytup = tup * 2 # tuple is repeated 2 times
print(mytup)
print(4 in tup) # output : False
print(2 in mytup) # output : True
print(len(tup)) # output : 3

child = tup[2:5] # slice operation child = (3,4,5)
print(child) # output : (3, 4, 5)

#------------------------------------------------------------------------------------------

a,b,c = child # unpacking tuple
print(a) # output : 3
print(b) # output : 4
print(c) # output : 5

print(max(child)) # output : 5
print(min(child)) # output : 3
#-----------------------------------------------------------------------------------------





