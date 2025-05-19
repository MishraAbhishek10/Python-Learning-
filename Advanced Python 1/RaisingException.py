# now we will try to raise our custon exceptions

a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

if(b==0):
    raise ZeroDivisionError("You can't divide by zero") # this will raise a ZeroDivisionError(crash the program here)
else:
    print(a/b)