class employee:
    a=1

class programmer(employee):
    b=2

class manager(programmer):
    c = 3


obj1 = employee()

print(obj1.a) # print the attribute of a only = 1
#print(obj1.b)     # shows an error that b attru=ibute is not present in employee class

obj2 = programmer()
print(obj2.a,obj2.b) # now it will print the attributes of employee as well as programmer

obj3 = manager()

print(obj3.a,obj3.b,obj3.c)

