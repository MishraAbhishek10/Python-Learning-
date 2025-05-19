#Loops

j = 0
while j<5: # or  while(j<5)
    print(j) # prints numbers from 0 to 4
    j += 1

l = [1,"Harry",10,"Shubh","tony"]
k = 0
while(k < len(l)):
    print(l[k]) # prints elements of list l
    k += 1

#---------------------------------------------------------------------------------------------
for item in l:
    print(item) # prints elements of list l
#---------------------------------------------------------------------------------------------
#for loop with else statement
for item in l:
    print(item) # prints elements of list l
else:
    print("done")

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------


# i is by default initialized to 0 and default step is 1
for i in range(5):
    print(i) # prints numbers 0 through 4

#----------------------------------------------------------------------------------------------

# i is initialized with 1 but default step is 1
for i in range(1, 5):
    print(i) # prints numbers 1 through 4

#------------------------------------------------------------------------------------------------
# i is initialized with 1 and step is 2
for i in range(1, 10, 2):
    print(i) # prints numbers 1, 3, 5, 7, 9

#-------------------------------------------------------------------------------------------------
# For Loops with Strings
# for loop can iterate over each character in a string
for char in "Hello, World!":
    print(char)

