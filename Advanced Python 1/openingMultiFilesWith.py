#You can now use multiple context managers in a single with statement more cleanly using the parenthesised context manager 
with ( open('myfile.txt') as f1, open('file.txt') as f2 ):
    # Process files
    print(f1.read())
    print(f2.read())
