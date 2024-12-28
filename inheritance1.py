class father:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)

        
class daughter(father):
    def __init__(self,name):
        self.name=name
    def show1(self):
        print(self.name)


x=father("narasimha")
x.show()
y=daughter("meghana")
y.show1()
y.show()                 #uses parent class function
