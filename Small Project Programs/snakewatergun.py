import random

#snake : 1
#water : -1
#gun : 0
com = random.choice([-1,0,1])
youstr = input("Enter a geuss: ")
youDict = {"s":1 , "w" : -1, "g" : 0}
you = youDict[youstr]


if(com == you):
    print("Draw !")

else:
    if(com==1 and you==-1):
        print("You Lose !")
    elif(com==1 and you==0):
        print("You Won !")
    elif(com==0 and you==1):
        print("You Lose !")
    elif(com==0 and you==-1):
        print("You Won !")
    elif(com==-1 and you==0):
        print("You Lose !")
    elif(com==-1 and you==1 ):
        print("You Won !")
    else:
        print("Something went wrong !")

    

