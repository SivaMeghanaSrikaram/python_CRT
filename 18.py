class mathematics:
    def addnumbers(x,y):    #self is not used here bcoz it is static method..self is for object but here we willexecute static method with class name.
        return x+y


x=staticmethod(mathematics.addnumbers)
print(x(4,2))
        
