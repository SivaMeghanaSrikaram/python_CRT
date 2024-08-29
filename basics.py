print("Name: S.Meghana")
print("Mobile no:9999999999")
print("CSE-2")
print()
print(25)
print(245.88)
print(False)
print("PYTHON")
print(10+5j)
print("----------------------")
a=10
b=78
c=35
print(a,b,c)
print(a,b,c,sep=',')
print(a,b,c,sep='+')
print(a,b,c,sep='   ')
print(a,b,c,sep='@')
print("------------------------")
print("Hello")
print("Rise")
print("People")
print("Hello",end=' ')
print("Rise",end=' ')
print("People")
print("------------------------")
x=open('new.txt','w')
print("python is very easy and our trainer is from chennai",file=x)
x.close()
print("------------------------")
s1='My name is meghana'
s2="My brother's name is abhi"
s3="I am learning 'PYTHON' language"
s4='''S.Meghana
56-364/B, Lawerpet
Ongole-523001'''
print(s1)
print(s2)
print(s3)
print(s4)
print("------------------------")
lan="python"
ver=3.14
fee=2500
#o/p:-I am learning python version 3.14 and the course fees is Rs.2500
print("I am learning",lan,"version",ver,"and the course fees is Rs.",fee)#here we are using ',' operator to concatenate
#here the disadvantage is the extra space is coming at the concatenation of Rs
print("I am learning "+lan+" version "+str(ver)+" and the course fees is Rs."+str(fee)) #here we are using '+' operator to concatenate
#disadv is there is no space......we should give space within the double quotes and also we cannot combine string and values
#FORMATE SPECIFIERS
print("I am learning %s version %.2f and the course fees is Rs.%d" %(lan,ver,fee))
#F-STRING
print(F"I am learning {lan} version {ver} and the course fees is Rs.{fee}")
#FORMATE
print("I am learning {} version {} and the course fees is Rs.{}".format(lan,ver,fee))

