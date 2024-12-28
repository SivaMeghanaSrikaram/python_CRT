class Father:
    fathername=''
    def father(self):
        print(self.fathername)

class Mother:
    mothername=''
    def mother(self):
        print(self.mothername)
  

class son1(Father,Mother):
    name=''
    def show(self):
        print(self.name)
        print(self.fathername)
        print(self.mothername)

class son2(Father):
    name=''
    def show1(self):
        print(self.name)
        print(self.fathername)



s1=son()
s1.name='lava'
s1.fathername='ram'
s1.mothername='sita'
s2=son2()
s2.name='kusha'
s2.fathername='ram'
s2.show1()
