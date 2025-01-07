try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a/b #this is enough in try block
    print(c)
    
except Exception as e:   #e here is an object
    print("can't divide with zero")
    print(e)
    
else:
    print("Your prog is successful")
