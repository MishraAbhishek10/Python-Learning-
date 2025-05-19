# Strings 

a = "Abhishek " # double quoted string 
b = 'Ayrisha ' # single quoted string
c = '''I am a good boy''' # triple quoted string
print(a+b+c)
# Output: Abhishek Ayrisha I am a good boy
# Strings are immutable in Python. You cannot change the value of a string after it's been created
# Strings are sequences of characters. You can access each character in a string using indexing.

#------------------------------------------------------------------------------------------------------------#

# STRING SLICING : String slicing is a way to extract a subset of characters from a string. It's done using

l = len(a)
print(l)

shortname = a[0:4]  # Extracts the first 4 characters from the string included 0 excluded 4
print(shortname) # Output: Abhi

#------------------------------------------------------------------------------------------------------------#

# NEGATIVE STRING SLICING : If you want to start from the end of the string, you can use a negative number as the start index.

print(a[-4: -1]) # Output: ek
print(a[1:4])
print(a[0:]) # Output: Abhishek same as print(a[0:n-1])
print(a[:6]) # Output: Abhish same as print(a[0:6])

#--------------------------------------------------------------------------------
name = input("Enter name : ")
print(f"Good Morning {name}") # f string used to avoid traditional way of concatenation

#--------------------------------------------------------------------
#chaining of replace function
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
'''
#print a new string but not change the original string that is why string is immutable 
print(letter.replace("<|Name|>","Abhishek").replace("<|Date|>","09 May 2025"))


