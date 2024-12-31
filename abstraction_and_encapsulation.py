class base:
    def __init__(self):
        self.__a=32
        print(self.__a+10)



class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self.__a)


#d1=derived()       #error bcoz private variable
b1=base()
#print(b1.__a)      #here also error bcoz we cannot print like this outside
        
