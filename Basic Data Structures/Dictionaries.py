# Dictionary :

'''
    # A dictionary is a collection of key-value pairs. 
    # It is an unordered collection of items that can be of any data type, including strings, integers, floats, and other dictionaries. 

    # Dictionaries are mutable, meaning they can be modified after creation. 
    # They are also dynamic, meaning they can grow orshrink as items are added or removed.
'''
#------------------------------------------------------------------------------------------------------
dic = {} # Create an empty dictionary
print("DAA marks : ")
marks = {
    "Abhishek" : 50,
    "Ayrisha" : 50,
    "Pranav" : 38,
    "Saini" : 44
}
# Accessing values in dictionary :
print(marks,type(marks))
print("Abhishek's marks : ", marks["Abhishek"])
print("Ayrisha's marks : ", marks["Ayrisha"])

print(marks.items()) # returns a list of tuples containing all key-value pairs
# OUTPUT : dict_items([('Abhishek', 50), ('Ayrisha', 50), ('Pranav', 38), ('Saini', 44)])

print(marks.keys()) # returns a view object that displays a list of all keys in the dictionary
# OUTPUT : dict_keys(['Abhishek', 'Ayrisha', 'Pranav', 'Saini'])

print(marks.values()) # returns a view object that displays a list of all values in the dictionary
# OUTPUT : dict_values([50, 50, 38, 44])

print(marks.get("Abhishek")) # returns the value for the given key if it exists
# OUTPUT : 50



marks.update({"Saini" : 30 , "Pranav" : 40})
print(marks)

val = marks.pop("Pranav") # removes the item with the specified key and returns the value of the removed item
print(val) 



print(marks)








#------------------------------------------------------------------------------------------------------------
# Advantages of dictionary :
# 1. Fast lookups : Dictionaries allow for fast lookups, with an average time indexed with keys 
# 2. mutable : Dictionaries are mutable, meaning they can be modified after creation.
# 3. Unique keys : Dictionaries can have unique keys
# 4. Flexible data structure : Dictionaries can store a wide range of data types, including
# 5. Easy modification : Dictionaries can be modified after creation, making them useful for dynamic
# ----------------------------------------------------------------------------------------------------------
# Disadvantage of dictionary :
# 1. Unordered : Dictionaries are unordered, meaning that the order of the key-valu
# 2. Key must be unique : Dictionaries require that each key be unique, which can
# 3. Slow insertion and deletion : Inserting and deleting items from a dictionary can be slow
# 4. Memory usage : Dictionaries can consume a lot of memory, especially if they contain list of list 
# 5. Limited support for nested data : Dictionaries do not support nested data structures
# ----------------------------------------------------------------------------------------------------------




