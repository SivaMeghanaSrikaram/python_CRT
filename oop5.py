class Person:
    static_count=0    #static keyword is used to represent static variable
    def __init__(self):
        Person.static_count+=1
        print(Person.static_count)
    

p1=Person()
p2=Person()
p3=Person()

#WE CAN OR CANNOT US USE static keyword
