try:
    a = int(input("Enter a number : "))
    b = int(input("Enter another number : "))
    print(a/b)

#if try block is not executed then except block will be executed
except ZeroDivisionError as z:
    print(z)
except Exception as e:
    print(e)

# finally block will be executed in any case but this is not the correct reason,
# print("thank you") will also run in any case So why finally ??

finally:
    print("thank you")

# if this code is part of the function and we returned some value from try , except then also the finally
# block will be executed
