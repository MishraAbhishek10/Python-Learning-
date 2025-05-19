# we can define custom behavior of operators 
class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self,num):  # operator overloading 
        return self.n + num.n
    
    def __mul__(self,num):
        return self.n*num.n
    
    

n = Number(1)
m = Number(2)

print(n+m) # it will show error without using it operator overloading
print(n*m)

