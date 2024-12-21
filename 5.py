def frmv(a,b):#a,b are formal parameters
     c=a+b
     d=a-b
     return c,d
a=int(input())
b=int(input())
x,y=frmv(a,b)#calling function(a,b are actual parameters)(function returns multiple values)
print(x,y)
