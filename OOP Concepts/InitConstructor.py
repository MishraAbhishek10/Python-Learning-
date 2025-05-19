class employee:
    language = "Python"
    salary= 1200000

    #def __init__(self): # dunder method called automatically 
    #    print("Creating object")

    def __init__(self,name,language,salary):
        self.name = name
        self.language  = language
        self.salary = salary

    

#harry = employee()
#harry.name = "Harry"

harry = employee("Harry","Java",1300000) # we can modify the constructor arguments 
print(harry.name,harry.language,harry.salary)

