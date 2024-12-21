def cbv(a):   #formal parameter
    print(a)
    print(id(a))
    a=a+2
    print(a)
    print(id(a))

a=5
print(a)
print(id(a))

cbv(a)         #actual parameter

print(a)
print(id(a))
