class Person:
    def __init__(self,name,age):  #name and age are instance variables which depends on object when it is created,
                                #self is present object which we will give down
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
    def decide(self):
        if(self.age>=18):
            print(self.age,"age is major")
        else:
            print("minor")
            

p1=Person("Meghana",2)
p2=Person("Lavanya",50)
p1.show()
p1.decide()
p2.show()
p2.decide()



