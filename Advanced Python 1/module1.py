def func():
    print("Hello")

#func()

#print(__name__)  # if run this file then it will print __main__ 
#otherwise it will print the name of the module where this function is defined

if(__name__ == "__main__"): # this is a guard clause : only print if this script is run directly in this file
    func()
    print(__name__)
    