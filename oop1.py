class person:
    age=20      #static variable bcoz p1 and p2 objects are using.



p1=person()
print(p1.age)
print(person.age)
p2=person()
print(person.age)   
