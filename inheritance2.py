class base:
    def __init__(self):
        self._a=32           #"_a"  is a protected variable
        print(self._a)
        
class derived(base):
    def __init__(self):
        base.__init__(self)  #identation will not use here
        print(self._a+2)


class derived1(derived):
    def __init__(self):
        derived.__init__(self)  #identation will not use here
        print(self._a+3)
        

d1=derived1()
