p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

msg = input("Enter comment : ")

# The in keyword returns True if a value exists in a sequence and False otherwise.
# (like list, string, tuple, set, or dictionary).

if((msg in p1) or (msg in p2) or (msg in p3) or (msg in p4)):
    print("Spam detected")

else:
    print("Not spam")

s = "Harry is a good boy."
print("Harry" in s) # Output: True

post = input("Enter your post: ")
#convert to lower to make the search case insensitive
if "Harry".lower() in post.lower():
    print("This post is talking about harry")

else :
    print("This post is not talking about harry")

