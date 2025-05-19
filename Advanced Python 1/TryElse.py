try:
    a = int(input("Enter a number : "))
    b = int(input("Enter another number : "))
    print(a/b)

#if try block is not executed then except block will be executed
except ZeroDivisionError as z:
    print(z)
except Exception as e:
    print(e)

#if try block successfully Executed then else will be executed
else:
    print("thank you")
