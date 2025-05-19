class employee:
    lang = "python"
    sal = 1200000

    
    def getInfo(self):  # we can also use some variable name in place of self
        print(f"language = {self.lang} , salary = {self.sal}" )
    
    @staticmethod  # used when there is no need to pass a parameter  OR use greet(self)
    def greet(): 
        print("Hello,Good Morning")

harry = employee()
harry.lang = "Java"
harry.greet()
harry.getInfo()
employee.getInfo(harry)  #the upper harry.getInfo() will work same way as this code

