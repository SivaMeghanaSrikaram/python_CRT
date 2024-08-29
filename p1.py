#write a python program to read 5 numbers  cfrom the user and find its sum and avg
n1=int(input('Enter the 1st number:'))
n2=int(input('Enter the 2nd number:'))
n3=int(input('Enter the 3rd number:'))
n4=int(input('Enter the 4th number:'))
n5=int(input('Enter the 5th number:'))
print("Numbers are: {},{},{},{},{}".format(n1,n2,n3,n4,n5)) #or print("Numbers are:",end=' ');print(n1,n2,n3,n4,n5,sep=',')
s=n1+n2+n3+n4+n5
print('Sum=',s)
avg=s/5
print('Average=',avg)

