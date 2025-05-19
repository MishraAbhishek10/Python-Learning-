from functools import reduce  # we need to import this to use reduce

# MAP EXAMPLE - 
l = [1,2,3,4,5]

sqr = lambda x: x*x

sqList = map(sqr,l) # here sqList is a map object
print(type(sqList)) # <class 'map'>

print(list(sqList))

#----------------------------------------------------------------------------------------------------------

# FILTER EXAMPLE -

# function to check odd/eevn or make lambda fuction
def even(n):
    return n % 2 == 0

onlyEven = filter(even,l)  # here onlyEven is a filter object
print(type(onlyEven))    # <class 'filter'>

print(list(onlyEven)) # output : [2,4]

#----------------------------------------------------------------------------------------------------------

# REDUCE EXAMPLE -

# we can use lambda function here as well
def sum(a,b):
    return a+b

mul = lambda x,y: x*y

print(reduce(sum,l))  #((((1 + 2) + 3) + 4) + 5) = 15 sequential computation 
print(reduce(mul,l))   # 1*2*3*4*5 = 120 sequential computation







