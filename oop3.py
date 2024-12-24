class Person:
    def __init__(self,name,age):  #name and age are instance variables which depends on object when it is created,
                                #self is present object which we will give down
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)


p1=Person("Meghana",20)
p2=Person("Lavanya",50)
p1.show()
p2.show()



