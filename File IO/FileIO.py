f = open("myfile.txt")
# ... rest of your code
data = f.read()
# f.write("Abhishek Mishra") ----> give error bcz file is not in write mode
print(data)
f.close()

#--------------------------------------------------------------------------

g = open("myfile.txt","r+")
# ... rest of your code
d = g.read()
print(d)
g.write(" Abhishek Mishra ")
g.close()
#--------------------------------------------------------------------------------
f = open("myfile.txt")
lines = f.readlines()
print(lines)
f.close()

#---------------------------------------------------------------------------------
f = open("myfile.txt")
line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()
#-----------------------------------------------------------------------------
st = "Hello, Good morning"
fl = open("file.txt" , "w")
fl.write(st)
fl.close()

