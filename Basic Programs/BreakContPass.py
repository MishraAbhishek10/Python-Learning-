# Break : immidiate exit if the condition match 
# Continue : skip this iteration and move to the next one
# Pass : Eat fivestar-do nothing and move to the next iteration

for i in range(100):
    if(i%2 != 0):continue
    if(i==10): pass # do nothing and move to the next iteration
    if(i>20): break
    print(i)

# if we leave it without pass it willl give indentation error 
l = [1,2,3,4]

for j in l: # or for j in range(len(l)):
    pass # did nothing and move for next

#------------------------------------------------------------------------------
n = int(input("Enter a number : "))

for i in range(1,n+1):
    print("*"*i)

#--------------------------------------------------------------------------------
for i in range(0,n+1):
    print(" "*(n-i+1) + "*"*((2*i)+1))

#-------------------------------------------------------------------------------

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n, end="")

    else :
        print("*" , end="")
        print(" "*(n-2) , end="")
        print("*" , end="")
    print(" ")











    