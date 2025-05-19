def func():
    try:
        a = int(input("Enter a number : "))
        b = int(input("Enter another number : "))
        print(a/b)
        return

    except ZeroDivisionError as z:
        print(z)
        return
    
    except Exception as e:
        print(e)
        return

    #if we remove finally it will not be printed 
    finally:
        print("thank you")


func()