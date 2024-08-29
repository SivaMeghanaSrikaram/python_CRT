import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print('--------------------')
#about varaiables
a=85
print(a,type(a))
b=687.54
print(b,type(b))
c='True'
print(c,type(c))
d=4+2j
print(d,type(d))
x='hi'
print(x,type(x))
print('--------------------')
name,age,year='meghana',20,'3rd year'
print('name=',name)
print('age=',age)
print('year=',year)
print('--------------------')
#swapping in general
a=25;b=10
temp=a
a=b
b=temp
print('after swapping')
print(a,b)
print('--------------------')
#swapping in general have another method wrote in note book
#swaping in python
a=25;b=10
a,b=b,a
print('after swapping')
print(f'a={a}')
print(f'b={b}')
print('--------------------')
y=85
print(y)
y=y+10*12
print(y)
#deleting
del y
#print(y) #error
print('--------------------')
#IDENTIFIERS
age=54
_no=76
#1a=25 #error(do not start with number)
If=20
iF=20
#if=20 #error(do not use keywords as identifiers0
firstname='hi'
#first name='hello' #error(should not put blankspaces in b/w)
first_name='meg'
#email@id='rise@gmail.com' #error(should not use special symbols in identifiers)
print('--------------------')
#using i/p function
name=input('enter ur name:')
age=int(input('enter ur age:'))
cn=input('what is ur college name?:')
fee=int(input('enter ur fee:'))
feepermon=fee//12
print("ur name is {}, ur age is {} and ur clg name is {}".format(name,age,cn))
print(f'fee per month is {feepermon}')
print('--------------------')
#mutable and immutable datatypes
a=10
print(a,id(a))# int is immutable bcoz add of this and nxt is diff
a=a*3
print(a,id(a))
b=[12,13,14,15]
print(b,id(b))
b.append(16)
print(b,id(b))
b[0]=2
print(b,id(b))
b.append
