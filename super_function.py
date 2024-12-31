class base:
    def __init__(self):
        self._a=32           #"_a"  is a protected variable
        print(self._a)
        
class derived(base):
    def __init__(self):
        super().__init__()  #identation will not use here,super() is used in the place of parent class and no need of self
        print(self._a+2)


class derived1(derived):
    def __init__(self):
        super().__init__()#identation will not use here and no need of self
        print(self._a+3)
        

d1=derived1()
