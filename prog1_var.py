def cse2():
    global a #whenever global variable need to be use in function this line is manditory
    a=a*2
    print(a)
    print(id(a))



a=5
print(a)
print(id(a))
cse2()
print(a)    #change of a is for the out side the function also
print(id(a))
