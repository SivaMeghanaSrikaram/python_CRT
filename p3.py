#write a python program to read a number n from the user and compute n+nn+nnn
a=input("Enter a number n:")
aa=a+a
aaa=a+a+a
s=int(a)+int(aa)+int(aaa)
print("The value is:",s)

#or s=int(a)+int(a+a)+int(a+a+a)
