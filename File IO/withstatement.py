f = open("file.txt")
print(f.read())
f.close

# the same can be written using with statement we don't need to close the file manually or explicitly 

with open("file.txt") as f:
    print(f.read())


# You can now use multiple context managers in a single with statement more cleanly using the parenthesised context manager 

with (open('file.txt') as f1,open('myfile.txt') as f2): # or with open('file.txt') as f1,open('myfile.txt') as f2 :

    # Process files  
    print(f1.read())
    print(f2.read())
