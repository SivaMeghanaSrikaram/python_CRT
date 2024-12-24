class Person:
    def __init__(self,name,age):  #name and age are instance variables which depends on object when it is created,
                                #self is present object
        self.name=name
        self.age=age


p1=Person("Meghana",20)
p2=Person("Lavanya",50)
print(p1.age,p1.name)
print(p2.age,p2.name)
