# format was used befre f strings 

a = "{} is a Good boy".format("Golu")
print(a)  # Output: Golu is a Good boy

b = "{} is a Good {}".format("Harry" , "Boy")
print(b)  # Output: Harry is a Good Boy


c = "{} is a Good {} and {} is a Good {}".format("0Harry" , "1Boy" , "2Rohan" , "3Boy")
print(c)  # Output: Harry is a Good Boy and Rohan is a Good Boy

# general order of format is 0 , 1 , 2 , 3 but we can change it also 

d = "{1} is a {0} {2}".format("Good","Harry","Boy")
print(d)  # Output: Harry is a Good Boy
