class employee:
    language = "python" # class variable or class attribute
    salary = 1200000

harry = employee()
harry.name = "Harry" # instance(object) variable or instance attribute
print(harry.name,harry.language,harry.salary)

#-----------------------------------------------------------------------------------------------------------
# instance attributes takes precedence over class attributes during assignment & retrieval 

rohan = employee()
rohan.name = "Rohan"
rohan.language = "java"
print(rohan.name,rohan.language,rohan.salary) # instance attributes takes precedence over class attributes during retrieval
