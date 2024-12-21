def cbrf(a):
    print(a)
    print(id(a))
    a.append("cse")
    print(a)
    print(id(a))

a=["rise"]
print(a)
print(id(a))
cbrf(a)
print(a)
print(id(a))
