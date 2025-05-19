class employee:
    a = 1
    # we use cls or any variable name  instead of self because 
    # we want to show class attribute even when instance attribute tried to change it's value 

    @classmethod  # Decorator : it will only show class attribute 
    def show(cls):  
        print(f"the class atrribute is {cls.a}")


obj = employee()
obj.a = 45  # instance attribute 

obj.show()  # 1
