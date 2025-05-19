
class employee:
    def __init__(self): # constructor 
        print("constructor of employee")

    
    a=1

class programmer(employee):
    def __init__(self):  # constructor 
        super().__init__()
        print("constructor of progarmmer")
    
    b=2

class manager(programmer):
    def __init__(self): # constructor 
        super().__init__() # it will call the constructor of it's parent class 
        print("constructor of manager")

    c = 3

# Now if we use "super().__init__()" in a child class it will also called the constructor of it's parent class

#obj1 = employee() 
#obj2 = programmer()    
obj3 = manager()    # constructor of employee,programmer and manager class will be called 


# if "super().__init__()" is not used then the constructor of individual classes will be called 






