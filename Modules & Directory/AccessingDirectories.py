import os

#specify directory yo want to access
directory_path = '/'

#list all files in the directory
contents = os.listdir(directory_path)

#print each file 
for item in contents:
    print(item)
