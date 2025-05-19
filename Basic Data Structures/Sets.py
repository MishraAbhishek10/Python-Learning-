# SETS : set is a collection of unique elements(unordered).
# SETS : set is mutable.
#----------------------------------------------------------------------------------------
#empty set
st = set()
print(type(st))

#set with elements
s = {5,1,2,4,1,2,"Hello",3,5,5,"A"} # duplicate elements are not allowed in set so it will automatically ignored
print(s)  #output : {1, 2, 3, 4, 5, 'A', 'Hello'}

s1 = {20,17,30,12,33,50,11}
print(s1) #output :{33, 17, 50, 20, 11, 12, 30}
#----------------------------------------------------------------------------------------
# SET METHODS -
# add() : add an element to the set
# discard() : remove an element from the set if it exists (it will not throw an error if the element is not in the set)
# remove() : remove an element from the set if it exists(if element is not present it will throw an error)
#----------------------------------------------------------------------------------------
s2 = {1,2,3,4,5}

s2.add(10)
print(s2)     #output : {1, 2, 3, 4, 5, 10}

s2.discard(1) 
print(s2) #output : {2, 3, 4, 5, 10}

s2.remove(3)
print(s2) #output : {2, 4, 5, 10}

s2.pop()
print(s2) #output : {4, 5, 10}

a = {1,2,4,7}
b = {1,4,5,6}
print(a.union(b))  #output : {1, 2, 4, 5, 6, 7 }
print(a.intersection(b)) #output : {1, 4}

print(a-b) #output : {2, 7}
print(a.difference(b)) #output : {2, 7}

c = {1,2}
print(c.issubset(a)) #output : True
print(a.issuperset(c)) #output : True

c.clear()
print(c) #output : set()  #clear() method is used to remove all elements from

p = {1,2,3,4,5,6}
p.pop()
print(p) #output : {2, 3, 4, 5, 6} removes arbitrary element from the set 

q = set()
q.add(18)
q.add("18")
print(q) #output : {18, '18'} #set can have duplicate values but they 

#-------------------------------------------------------------------------------------------------
# SET of list 
#R = {4,5,[1,2]}  #In Python, sets can only contain immutable (hashable) objects . Lists are mutable, so they cannot be added to a set.  
#output : TypeError:
#print(R) 
#-------------------------------------------------------------------------------------------------

