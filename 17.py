class A:
    def myname(self):
        print("my class is A")


class B(A):
    def myname(self):
        print("my class is B")


class C(A):
    def myname(self):
        print("my name is C")


class D(C,B):
    pass


d=D()
d.myname()      #it goes to C bcoz it checks in order (from bottom to top)

