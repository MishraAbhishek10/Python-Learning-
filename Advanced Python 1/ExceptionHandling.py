try:
    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))
    print("Sum of two numbers is : ", a//b)

except ValueError as v:
    print(v)

except ZeroDivisionError as z:
    print(z)
except Exception as e:
    print(e)

print("thank you")

