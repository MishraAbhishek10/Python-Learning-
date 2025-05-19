class employee: # parent class 
    company = "ITC"
    def show(self):
        print(self.name , self.salary)


class programmer(employee): # derived class 
    company = "ITC Info"

    def showlang(self):
        print(self.name,self.lang)


a = employee()
b =programmer()
print(a.company,b.company)

