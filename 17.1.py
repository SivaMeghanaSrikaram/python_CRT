class A:
    def myname(self):
        print("my class is A")


class B(A):
    def myname(self):
        print("my class is B")


class C(A):
    def myname(self):
        print("my name is C")


class D(B,C):
    pass


print(D.__mro__)
print(C.mro())

