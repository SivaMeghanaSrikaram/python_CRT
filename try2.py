try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a/b #this is enough in try block
    print(c)
except Exception:
    print("can't divide with zero")
    print(Exception)
else:
    print("Your prog is successful")
