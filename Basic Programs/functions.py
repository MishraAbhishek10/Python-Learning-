#function definition 
def func():
    a = int(input("Enter a number : "))
    b = int(input("Enter second number : "))
    sum = a+b
    #print(sum)
    return sum 

a = func() #function call
print(a)

#-----------------------------------------------------------------

def greet(name):
    print("Hello, " + name + "!")

greet("John") #function call

#------------------------------------------------------------------
#Default parameter 

def fun(name = "Stranger"):
    print("hello, " + name)

fun() #output : hello, Stranger
fun("Golu") 

