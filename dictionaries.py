'''--------DICTIONARIES concept--------'''

#--------ACCESSING---------

d1={'name':'anil','rollno':502,'per':85.76}
print(d1) #we will get all items
print(len(d1))
print(d1.keys())  #to get keys
print(*d1)        #to get keys
print(d1.get('name',"given key not present")) #to get values
print(d1.get('branch',"given key not present"))#to get values
print(d1.setdefault('branch',"given key not present"))#to get values
print(d1.setdefault('branch'))#to get value
print(d1.values())#to get value
print(d1['rollno']) #used [] bcoz generally the o/p of dict is in []

x=d1.items() #to get all items
print(x)

#------MODIFICATION---------

d1['per']=95.89
print(d1)   #modifying a value

d1['branch']='CSE'
print(d1)   #adding an extra key and value

d2={"college":"Rise"}
d1.update(d2)
print(d1)   #adding one dict to other

#-------DELETION--------

del d1['rollno']
print(d1)

d1.popitem()
print(d1)  #removes last record


d1.pop('name')
print(d1)  #removes given key and value

d1.clear()
print(d1)  #removes all the records and the o/p will be empty brackets--->{}

del d1
#print(d1) #datastructure is deleted if we try to print error msg will be shown


''' print(d1*3),print(d1+d2) these repetition operators works only on any datastructure except dict and set'''

#-----COPY OPERATION-------

x={'name':'anil','rollno':502,'per':85.76}
y=x   #copying by using a variable
print(x)
print(y)
print(id(x))#addresses of x and y are same bcoz it is not real copy
print(id(y))

z=x.copy()
print(z)
print(id(x)) #addresses are diff bcoz it will make a real copy
print(id(z))

'''copy module can be wriiten as
import copy
z=copy.copy(x) '''

#CREATING a dictionary fromkeys()

a=['name','rollno','per']
b=['meghana','502','99.87']
c=dict.fromkeys(a,b)
print(c)



