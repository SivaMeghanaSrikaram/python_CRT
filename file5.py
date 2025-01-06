x=open('s3batch.txt','r')
c=0
for i in x:
    print(i)
    c+=1
print(c)
x.close()
