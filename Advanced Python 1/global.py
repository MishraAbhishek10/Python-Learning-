num = 100 # Global variable
a = 1000
def func():
    num = 4 # Local variable 
    global a # Accessing global variable : value will be updated globally
    a = 10
    print(num)


print(num) # Output: 100 global variable

func()

print(a)