l = [1,100,3,500,20,50]

idx = 0
for item in l:
    print(f"at index {idx} item = {item}")


# Alternate way using enumerate() function
for idx, item in enumerate(l):
    print(f"at index {idx} item = {item}")