def frmv(a,b):#a,b are formal parameters
     c=a+b
     d=a-b
     return c,d
a=int(input())
b=int(input())
x=frmv(a,b)#x acts as tuple here to store multiple vaues i.e.,c,d(function returns multiple values)
print(x)
print(type(x))
