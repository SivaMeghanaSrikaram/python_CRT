try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a/b #this is enough in try block
    print(c)
except:
    print("can't divide with zero")
