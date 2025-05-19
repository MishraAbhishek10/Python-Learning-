age = int(input("Enter you age : "))

if(age%2==0):
    print("Even number")
else :
    print("Odd number")

if(age <= 0):
    print("Invalid age !!! Age can't be negative")
elif(age >= 18):
    print("You are eligible to vote")

else:
    print("You are not eligible to vote")
