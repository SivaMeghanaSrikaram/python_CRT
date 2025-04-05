a=int(input())
b=bin(a) #bin() converts the data to binary(0b)
print(b)
print(type(b))
b=b[2:]
d=int(b,2) #int(datatoconvert,data base)
print(d)


'''similary oct(a)--->(0o),
            hex(a)--->(0x) '''
            
