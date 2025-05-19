class employee:
    a = 1

    @classmethod  # Decorator : it will only show class attribute 
    def show(cls):  
        print(f"the class atrribute is {cls.a}")



# abstraction - encapsulation 

    @property
    def name(self):
        return f"{self.fname , self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]  # split the value and store in list form 
        self.lname = value.split(" ")[1] 

    



obj = employee()
obj.a = 45  # instance attribute 

obj.name = "code with"
print(obj.name)
print(obj.fname,obj.lname)

obj.show()  # 1
