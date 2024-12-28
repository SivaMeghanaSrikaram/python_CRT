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


s2=son2()
s2.name='abhishek'
s2.fathername='narasimha'
s2.show1()
