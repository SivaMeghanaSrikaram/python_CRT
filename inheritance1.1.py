class base:
    def __init__(self):
        self._a=32           #"_a"  is a protected variable

        
class derived(base):
    def __init__(self):
        base.__init__(self)  #identation will not use here
        print(self._a)
        

d1=derived()
