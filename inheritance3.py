class Father:
    fathername=''
    def father(self):
        print(self.fathername)

class Mother:
    mothername=''
    def mother(self):
        print(self.mothername)
  

class son(Father,Mother):
    name=''
    def show(self):
        print(self.name)
        print(self.fathername)
        print(self.mothername)


s1=son()
s1.name='abhishek'
s1.fathername='narasimha'
s1.mothername='lavanya'
s1.show()
