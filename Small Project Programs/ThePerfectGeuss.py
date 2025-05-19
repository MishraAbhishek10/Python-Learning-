'''
We are going to write a program that generates a random number and asks the user to 
guess it. 
If the player’s guess is higher than the actual number, the program displays “Lower 
number please”. Similarly, if the user’s guess is too low, the program prints “higher 
number please” When the user guesses the correct number, the program displays the 
number of guesses the player used to arrive at the number. 
Hint: Use the random module.

'''

import random
n = random.randint(1,100)
a = -1

attemt = 0
while(a != n):
    a = int(input("Geuss a Number: "))
    attemt += 1

    if(a > n):
        print("Your Geuss is more than the number")

    else:
        print("Your Geuss is less than the number")

print(f"You geussed the correct number {n} in {attemt} attempts")
    
